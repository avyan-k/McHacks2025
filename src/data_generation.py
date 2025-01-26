import datetime
import random
from enum import Enum
from task import *
from dev import Dev
import database

# List of example task names
TASK_NAMES = [
    "Fix login bug",
    "Add user authentication",
    "Improve database performance",
    "Implement dark mode",
    "Add search functionality",
    "Fix crash on startup",
    "Optimize image loading",
    "Add multi-language support",
    "Create admin dashboard",
    "Refactor payment module",
    "Fix password reset issue",
    "Implement notifications",
    "Upgrade backend framework",
    "Add file upload feature",
    "Fix scrolling issue",
    "Implement caching mechanism",
    "Improve API response times",
    "Fix layout alignment",
    "Add user roles and permissions",
    "Fix memory leak",
    "Enhance security measures",
    "Fix session expiration bug",
    "Redesign homepage",
    "Fix broken links",
    "Add analytics tracking",
    "Implement user feedback form",
    "Fix email delivery issue",
    "Add two-factor authentication",
    "Optimize query performance",
    "Fix video playback issue",
    "Create onboarding flow",
    "Improve accessibility features",
    "Implement feature flags",
    "Fix notification delay",
    "Add QR code generator",
    "Refactor legacy code",
    "Improve mobile responsiveness",
    "Fix timezone issues",
    "Add audit logging",
    "Fix cookie handling",
    "Implement autosave",
    "Improve test coverage",
    "Fix localization issues",
    "Add chatbot support",
    "Fix server-side rendering bug",
    "Optimize background tasks",
    "Add custom user avatars",
    "Fix database migration issue",
    "Implement role-based access control",
    "Improve error handling",
    "Fix loading spinner",
    "Add real-time collaboration",
    "Optimize CSS styles",
    "Fix search indexing",
    "Add bulk import feature",
    "Fix API authentication",
    "Improve file compression",
    "Add email templates",
    "Fix pagination issues",
    "Improve code documentation",
    "Add websocket support",
    "Fix image cropping tool",
    "Improve build pipeline",
    "Fix webhook delivery issues",
    "Add undo/redo functionality",
    "Fix performance regression",
    "Add reporting dashboards",
    "Implement mobile push notifications",
    "Fix data export issues",
    "Add live chat support",
    "Fix PDF generation issue",
    "Enhance UI animations",
    "Fix dropdown menu bug",
    "Add calendar integration",
    "Fix dependency conflicts",
    "Optimize server logs",
    "Fix user profile updates",
    "Add custom themes",
    "Improve deployment scripts",
    "Fix modal window bug",
    "Implement rate limiting",
    "Add payment gateway integration",
    "Fix infinite scrolling issue",
    "Improve session handling",
    "Fix duplicate entries",
    "Add email verification",
    "Fix error message display",
    "Optimize SQL queries",
    "Fix user logout issues",
    "Implement document preview",
    "Add advanced search filters",
    "Fix file download issues",
    "Improve CDN performance",
    "Fix upload timeout",
    "Add password strength meter",
    "Improve user activity tracking",
    "Fix sorting issues",
    "Add social media sharing",
    "Fix tooltip display",
    "Implement project templates",
    "Fix broken API endpoints",
    "Add import/export settings"
]

# Generate 10 developers
DEV_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]


def generate_data():
    devs = []
    # Generate 100 tasks
    random.seed(42)  # For reproducibility
    tasks = []

    for i in range(100):
        name = random.choice(TASK_NAMES)
        deadline = datetime.date.today() + datetime.timedelta(days=random.randint(1, 365))
        estimated_time = random.randint(1, 730)  # Estimated time in hours (up to 730 = ~1 month)
        priority = random.randint(1, 5)
        status=Status.INCOMING
        task = Task(name, deadline, estimated_time, priority, status)
        tasks.append(task)

    for i, name in enumerate(DEV_NAMES):
        dev_id = random.randint(10000000, 99999999)  # 8-digit ID
        experience_level = random.randint(1, 8)
        dev = Dev(dev_id, name, experience_level)
        devs.append(dev)

    return tasks, devs