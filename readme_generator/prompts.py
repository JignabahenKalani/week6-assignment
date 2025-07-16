from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.validator import Validator , ValidationError

def checkbox_non_empty(value):
    if not value or len(value)==0:
        return "Please select at least one option."
    return True

class MinLengthValidator(Validator):
    def __init__(self,min_length,message=None):
       self.min_length = min_length
       self.message = message or f"Please enter at least {min_length} characters."

    def validate(self, result):
        text = result.text
        if len(text.strip()) < self.min_length:
            raise ValidationError(message=self.message)
        
class EmailValidator(Validator):
    def validate(self, result):
        text = result.text
        if "@" not in text or "." not in text:
            raise ValidationError(message="Please enter a valid email address.")

            
def get_project_prompts():
    title = inquirer.text(
        message=" Enter your Project Title:",            validate=MinLengthValidator(5, "Project title cannot be empty.")
    ).execute()
        
    description = inquirer.text(
        message="Enter your Project Description:",            validate=MinLengthValidator(20, "Description must be at least 20 characters.")
    ).execute()

    installation = inquirer.text(
        message="Enter Installation Instructions:",
        validate=MinLengthValidator(10,"Installation instractions must be at least 10 characters.")
    ).execute()

    usage = inquirer.text(
        message="Enter Usage Instructions:",
        validate=MinLengthValidator(10, "Usage instructions must be at least 10 characters.")
    ).execute()

    license = inquirer.select(
        message="Select the License:",
        choices=[
            "MIT License",
            "GNU General Public License v3.0",
            "Apache License 2.0",
            "BSC 3-Clause License",
            "Creative Commons Zero v1.0 Universal",
            Separator(),
            "No License"
        ]
    ).execute()
    
    features = inquirer.checkbox(
        message="Select the Features:",
        choices=[
            "User Authentication",
            "Data Visualization",          
            "Real-time Notifications",
            "Multi-language Support",
            "Responsive Design",
            "API Integration",
            "Offline Mode",
            Separator(),
            "No Features"
        ],
        validate=checkbox_non_empty
    ).execute()

    technologies = inquirer.checkbox(
        message="Select the Technologies Used:",
        choices=[
            "HTML5"
            "CSS3",
            "Bootstrap 5",
            "JavaScript",
            "jQuery",
            "Python",
            "GitHub Pages",
            Separator(),
            "Other"
        ],
        validate=checkbox_non_empty
    ).execute()

    tests_responsive = inquirer.checkbox(
        message="Select if responsive testing is supported.",
        choices=[
            "Mobile Devices"
            "Laptops"
            "Desktops"
        ]
    ).execute()
        
    tests = inquirer.text(
        message="Enter Test Instruction:",
        default="No specific test cases provided yet."
    ).execute()

    contribution = inquirer.select(
        message="Would you like others to contribute to your project?",
        choices=["Yes", "No"]
    ).execute()
    
    contribution_guidelines = inquirer.text(
        message="Enter Contribution Guidelines:",
        default="Follow standard open source contribution practices."
    ).execute()

    author = inquirer.text(
        message="Enter Author Name:",
        validate=MinLengthValidator(3, "Please enter a valid author name (min 3 characters).")
    ).execute()

    email = inquirer.text(
        message="Enter Contact Email:",
        validate=EmailValidator()
    ).execute()

    confirm = inquirer.confirm(
        message="Do you want to generate the README file?",
        default=True
    ).execute()
    
    return{
        "title": title,
        "description": description,
        "installation": installation,
        "usage": usage,
        "license": license,
        "features": features,
        "technologies": technologies,
        "test_responsive" : tests_responsive,
        "tests": tests,
        "contribution": contribution,
        "contribution_guidelines": contribution_guidelines,
        "author": author,
        "email": email,
        "confirm": confirm
    }
        