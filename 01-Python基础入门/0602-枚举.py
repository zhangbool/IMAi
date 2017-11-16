from enum import Enum

month = Enum("Month", ("Jan", "Feb", "Mar", "Apri", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"))

print(month)

for item in month:
    print(item)

jan = month.Jan
print(jan)

# for name, member in month.enum_members.items():
#     print(name, "=>", member, ",", member.Value)


