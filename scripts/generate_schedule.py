#!/usr/bin/env python3
"""
Script to generate Jekyll schedule data from CSV file.
This script reads _events/schedule.csv and generates the appropriate data files
to populate the schedule page dynamically.
"""

import csv
import os
import re
from datetime import datetime, timedelta
import yaml

def parse_date(date_str):
    """Parse date string in format 'M/D/YY' and return ISO format."""
    if not date_str or date_str.strip() == '':
        return None
    
    try:
        # Handle different date formats
        if '/' in date_str:
            # Format: 8/26/25
            date_obj = datetime.strptime(date_str.strip(), '%m/%d/%y')
        else:
            # Try other formats if needed
            date_obj = datetime.strptime(date_str.strip(), '%Y-%m-%d')
        
        # Keep the original date as is - no year conversion needed
        return date_obj.strftime('%Y-%m-%d')
            
    except ValueError as e:
        print(f"Warning: Could not parse date '{date_str}': {e}")
        return None

def extract_homework_info(homeworks_str):
    """Extract homework information from the Homeworks column."""
    if not homeworks_str or homeworks_str.strip() == '':
        return None
    
    hw_str = homeworks_str.strip()
    
    # Extract homework number
    hw_match = re.search(r'HW(\d+)', hw_str, re.IGNORECASE)
    hw_num = hw_match.group(1) if hw_match else None
    
    # Extract specific dates and times from the homeworks column
    # Format examples: "HW1 out on 09/05 (Fri) 5:00pm", "HW1 due on 09/22 (Mon) 5:00pm"
    date_time_match = re.search(r'(\d{1,2}/\d{1,2})\s*\([A-Za-z]{3}\)\s*(\d{1,2}):(\d{2})(am|pm)', hw_str, re.IGNORECASE)
    
    if date_time_match:
        date_str = date_time_match.group(1)
        hour = int(date_time_match.group(2))
        minute = date_time_match.group(3)
        ampm = date_time_match.group(4).lower()
        
        # Convert to 24-hour format
        if ampm == 'pm' and hour != 12:
            hour += 12
        elif ampm == 'am' and hour == 12:
            hour = 0
        
        # Parse the date
        try:
            date_obj = datetime.strptime(date_str, '%m/%d')
            date_obj = date_obj.replace(year=2025)
            formatted_date = date_obj.strftime('%Y-%m-%d')
            formatted_time = f"{hour:02d}:{minute}:00"
        except:
            return None
    else:
        # Fallback for dates without time: "HW2 due (10/24)", "HW3 release (11/04)"
        date_match = re.search(r'\((\d{1,2}/\d{1,2})\)', hw_str)
        if date_match:
            date_str = date_match.group(1)
            try:
                date_obj = datetime.strptime(date_str, '%m/%d')
                date_obj = date_obj.replace(year=2025)
                formatted_date = date_obj.strftime('%Y-%m-%d')
                formatted_time = "17:00:00"  # Default to 3:00 PM
            except:
                return None
        else:
            return None
    
    # Extract action (out, due, grades release)
    action = None
    if 'out' in hw_str.lower():
        action = 'release'
    elif 'due' in hw_str.lower():
        action = 'due'
    elif 'grades' in hw_str.lower():
        action = 'grades'
    
    return {
        'hw_num': hw_num,
        'date': formatted_date,
        'time': formatted_time,
        'action': action,
        'description': hw_str
    }

def generate_lecture_data(row, lecture_num):
    """Generate lecture data from CSV row."""
    date = parse_date(row['Lecture Date'])
    if not date:
        return None
    
    # Determine lecture type
    overview = row['Overview'].strip() if row['Overview'] else ''
    topics = row['Topics'].strip() if row['Topics'] else ''
    
    # Check if this is a project presentation
    if 'Project Presentation' in overview or 'Project Presentation' in topics:
        return {
            'type': 'project',
            'date': f"{date}T17:00:00+03:30",  # 3:30 PM class time
            'title': 'Project Presentation',
            'overview': overview,
            'topics': topics,
            'content': topics
        }
    
    # Create title
    if overview and overview != 'No Lecture':
        title = overview
    elif topics and topics != 'No Lecture':
        title = topics
    else:
        title = f"Lecture {lecture_num}"
    
    # Handle special cases
    if 'No Lecture' in overview or 'No Lecture' in topics:
        return None
    
    lecture_data = {
        'type': 'lecture',
        'date': f"{date}T17:00:00+03:30",  # 3:30 PM class time
        'title': title,
        'overview': overview,
        'topics': topics,
        'lecture_num': lecture_num,
        'content': topics  # Add topics as content for course material column
    }
    
    return lecture_data

def generate_assignment_data(hw_info, row):
    """Generate assignment data from homework info."""
    if not hw_info or not hw_info['hw_num']:
        return None
    
    hw_num = hw_info['hw_num']
    action = hw_info['action']
    
    if action == 'release':
        # Assignment release - use exact date and time from homeworks column
        if 'date' in hw_info and 'time' in hw_info:
            date_str = hw_info['date']
            time_str = hw_info['time']
            return {
                'type': 'assignment',
                'date': f"{date_str}T{time_str}+03:30",
                'title': f"Homework {hw_num}",
                'hw_num': hw_num,
                'action': 'release'
            }
        else:
            # Fallback to lecture date
            date = parse_date(row['Lecture Date'])
            if not date:
                return None
            return {
                'type': 'assignment',
                'date': f"{date}T16:00:00+03:30",  # After lecture
                'title': f"Homework {hw_num}",
                'hw_num': hw_num,
                'action': 'release'
            }
    
    elif action == 'due':
        # Assignment due - use exact date and time from homeworks column
        if 'date' in hw_info and 'time' in hw_info:
            date_str = hw_info['date']
            time_str = hw_info['time']
            return {
                'type': 'due',
                'date': f"{date_str}T{time_str}+03:30",
                'title': f"Homework {hw_num} Due",
                'hw_num': hw_num,
                'action': 'due'
            }
        else:
            return None
    
    elif action == 'grades':
        # Grades release - use exact date from homeworks column
        if 'date' in hw_info:
            date_str = hw_info['date']
            time_str = hw_info.get('time', '17:00:00')  # Default to 3:00 PM
            return {
                'type': 'grades',
                'date': f"{date_str}T{time_str}+03:30",
                'title': f"Homework {hw_num} Grades Released",
                'hw_num': hw_num,
                'action': 'grades'
            }
        else:
            # Fallback to lecture date
            date = parse_date(row['Lecture Date'])
            if not date:
                return None
            return {
                'type': 'grades',
                'date': f"{date}T17:00:00+03:30",
                'title': f"Homework {hw_num} Grades Released",
                'hw_num': hw_num,
                'action': 'grades'
            }
    
    return None

def main():
    """Main function to process CSV and generate data files."""
    csv_file = '_events/schedule.csv'
    
    if not os.path.exists(csv_file):
        print(f"Error: CSV file {csv_file} not found!")
        return
    
    lectures = []
    projects = []
    assignments = []
    events = []
    lecture_num = 1
    
    print("Reading schedule CSV file...")
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Generate lecture/project data
            event_data = generate_lecture_data(row, lecture_num)
            if event_data:
                if event_data['type'] == 'project':
                    projects.append(event_data)
                else:
                    lectures.append(event_data)
                    lecture_num += 1
            
            # Generate assignment data from homeworks column
            hw_info = extract_homework_info(row['Homeworks'])
            if hw_info:
                assignment_data = generate_assignment_data(hw_info, row)
                if assignment_data:
                    if assignment_data['type'] == 'assignment':
                        assignments.append(assignment_data)
                    else:
                        events.append(assignment_data)
    
    # Sort all events by date
    all_events = lectures + projects + assignments + events
    all_events.sort(key=lambda x: x['date'])
    
    # Create _data directory if it doesn't exist
    data_dir = '_data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Generate lectures.yml
    print("Generating lectures.yml...")
    with open(os.path.join(data_dir, 'lectures.yml'), 'w', encoding='utf-8') as f:
        yaml.dump(lectures, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    # Generate projects.yml
    print("Generating projects.yml...")
    with open(os.path.join(data_dir, 'projects.yml'), 'w', encoding='utf-8') as f:
        yaml.dump(projects, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    # Generate assignments.yml
    print("Generating assignments.yml...")
    with open(os.path.join(data_dir, 'assignments.yml'), 'w', encoding='utf-8') as f:
        yaml.dump(assignments, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    # Generate events.yml
    print("Generating events.yml...")
    with open(os.path.join(data_dir, 'events.yml'), 'w', encoding='utf-8') as f:
        yaml.dump(events, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Generated {len(lectures)} lectures, {len(projects)} projects, {len(assignments)} assignments, and {len(events)} events")
    print("Schedule data files created successfully!")
    
    # Print summary
    print("\nSchedule Summary:")
    print("=" * 50)
    for event in all_events[:10]:  # Show first 10 events
        date = event['date'].split('T')[0]
        event_type = event['type'].upper()
        title = event['title']
        print(f"{date} | {event_type:10} | {title}")
    
    if len(all_events) > 10:
        print(f"... and {len(all_events) - 10} more events")

if __name__ == "__main__":
    main()
