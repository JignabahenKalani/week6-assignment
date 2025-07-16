class ReadmeCreator:
    def __init__(self,project_info):
        self.project_info = project_info
    
    tech_emojis = {
            "HTML5": "🌐",
            "CSS3": "🎨",
            "Bootstrap 5": "🅱️",
            "JavaScript": "✨",
            "jQuery": "🔧",
            "Python": "🐍",
            "GitHub Pages": "📄"
        }

    responsive_emojis = {
            "Mobile Devices": "📲",
            "Laptops": "💻",
            "Desktop": "🖥"
        }
    
    feature_emojis={
        "User Authentication": "✅",
        "Data Visualization" : "📊",
        "Real-time Notifications": "🔔",
        "Multi-language Support": "🌐",
        "Responsive Design": "📱",
        "API Integration": "🔌",
        "Offline Mode": "📴"
    }
    
    def generate_readme(self):
    
        readme_content = f"#📝 {self.project_info['title']}</h1>\n\n"
        readme_content += f"## 📘 Description\n{self.project_info['description']}\n\n\n"
        readme_content += f"## 📦 Installation\n{self.project_info['installation']}\n\n\n"
        readme_content += f"## 🛠️ Usage\n{self.project_info['usage']}\n\n\n"
        readme_content += (f"## 📄 License\n"f"{self.project_info['license']} - {self.project_info['license_line']}\n\n")



        readme_content += "## 🚀 Features\n\n"
        for feature in self.project_info['features']:
            emoji = self.feature_emojis.get(feature, "🔹")
            readme_content += f"{emoji} {feature}\n"
        readme_content += "\n"

        readme_content += "## 🛠️ Technologies\n\n"
        for tech in self.project_info['technologies']:
            emoji = self.tech_emojis.get(tech, "🔹")
            readme_content += f"{emoji} {tech}\n"
        readme_content += "\n\n"

        readme_content += "## 🧿 Design check Responsive\n\n"
        for test_responsive in self.project_info['test_responsive']:
            emoji = self.responsive_emojis.get(test_responsive, "🔹")
            readme_content += f"{emoji} {test_responsive}\n"
        readme_content += "\n\n"

        readme_content += f"## 🧪 Tests\n{self.project_info['tests']}\n\n\n"
        readme_content += f"## 🤝 Contribution\n{self.project_info['contribution']} - {self.project_info['contribution_line']}\n\n"
    
   

        readme_content += f"## 👤 Author\n{self.project_info['author']}\n\n\n"
        readme_content += f"## 📧 Email\n{self.project_info['email']}\n\n\n"

        if self.project_info.get("contribution_guidelines"):
            readme_content += f"## 🧾 Contribution Guidelines\n{self.project_info['contribution_guidelines']}\n\n"

        return readme_content
    
    def save_readme(self, filename='README.md'):
        with open(filename, 'w') as file:
            file.write(self.generate_readme())
        print(f"README file '{filename}' has been created successfully.")
        return filename

def generate_markdown(self):
    badge = self.generate_badge()
    return f"""# ***{self.project_info['title']}***
{badge}
## 📘 Description
{self.project_info['description']}
## 📦 Installation
{self.project_info['installation']}
## 🛠️ Usage
{self.project_info['usage']}
## 📄 License
{self.project_info['license']}
## 🚀 Features
{', '.join(self.project_info['features'])}
## 🛠️ Technologies
{self.project_info['technologies']}
## 🧿 Design check Responsive
{self.project_info['test_responsive']}
## 🧪 Tests
{self.project_info['tests']}
## 🤝 Contribution
{self.project_info['contribution']}
## 👤 Author
{self.project_info['author']}
## 📧 Email
{self.project_info['email']}
##  🤝 Contribution Guidelines
{self.project_info.get('contribution_guidelines', 'No contribution guidelines provided')}
## ✅ Confirmation
{self.project_info['confirm']}
Thank you

"""
