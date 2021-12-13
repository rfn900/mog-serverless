values = """{
"prop1": "val1",
"prop2": "val2",
"prop3": "val3"
}
"""
name1 = "john"
name2 = "sebo"
name3 = "jumboa"
values2 = (f"{{ \n"
           f" \"prop1\": \"{name1}\", \n"
           f" \"prop2\": \"{name2}\", \n"
           f" \"prop3\": \"{name3}\" \n"
           f"}}"
           )


print(values)
print(values2)
