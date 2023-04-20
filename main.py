#|String appender

text = "STRING"
Non_appended = ""
with open('toappend.txt', 'r') as f:
    Non_appended = f.readlines()
with open('appended.txt', 'a') as f:
    for line in Non_appended:
        f.write(text + " " + line)
