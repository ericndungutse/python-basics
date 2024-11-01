import re;
from data import text;

# Regex for phone numbers 545-2323, 545-232-2323, 545-232-2323 x2323, 545-232-2323 ext2323
# Types 33-0000, 313-443-2332, (250) 343-2323, 343-2323, 343-2323 x2323, 343-2323 ext2323
phone_regex = re.compile(r'''(
                         ((\d\d\d)|(\(\d\d\d\)))?  # Area code(Optional)
                         (\s|-)?                    # First separator - space or hyphen(-)
                         \d\d\d                     # First 3 digits
                         -                          # Separator - hyphen
                         \d\d\d\d                   # Last 4 digits
                         (\s((ext(\.)?\s)|x)(\d{2,5}))? # Extension(optional)
                         )
                         ''', re.VERBOSE);

# Regex patter for email
email_regex = re.compile(r'''
                        [a-zA-Z0-9._.+]+ # Username
                        @                # @ symbol
                        [a-zA-Z._+]+     # Domain name
                         ''', re.VERBOSE);



# Extract email and phone number from a text
extracted_phone_numbers = phone_regex.findall(text);
# REturn phone_number[0] from extracted_phone_numbers
all_phone_numbers = [phone_number[0] for phone_number in extracted_phone_numbers];
extracted_emails = email_regex.findall(text);

# Display
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_emails);

print(results)