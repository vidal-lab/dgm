#!/bin/bash

# Script to update the schedule from CSV file
echo "🔄 Updating schedule from CSV file..."

# Run the Python script to generate data files
python scripts/generate_schedule.py

if [ $? -eq 0 ]; then
    echo "✅ Schedule updated successfully!"
    echo "📊 Generated data files:"
    echo "   - _data/lectures.yml"
    echo "   - _data/assignments.yml" 
    echo "   - _data/events.yml"
    echo ""
    echo "🌐 The schedule page will now reflect the updated data."
else
    echo "❌ Error updating schedule!"
    exit 1
fi
