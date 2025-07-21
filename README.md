# ⏰ Time Calculator 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

A user-friendly GUI tool to calculate future times by adding hours/minutes to a starting time. Perfect for scheduling, work shifts, or travel planning!

## ✨ Features
- ✅ **AM/PM Support**: Input times like `3:30 PM` or `14:30`
- 📅 **Day Tracking**: Automatically detects day changes (e.g., "next day")
- 🌙 **Day-of-Week**: Optional weekday input (e.g., "Monday" → "Tuesday")
- 🛠️ **Error Handling**: Validates user inputs
- 🖥️ **Clean GUI**: Built with Tkinter (no extra dependencies)

## 🎯 Usage Examples
Start Time	Duration	Day	Output
3:30 PM	2:15	-	5:45 PM
11:45 PM	2:30	-	2:15 AM (next day)
10:00 PM	30:00	Friday	4:00 AM Sunday (2 days later)
