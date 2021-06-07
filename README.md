# WhatsApp-bot
That's a WhatsApp bot that enable you to join / quit groups and send messages to specific groups  

# Main features : 
- Verify if groups exist via urls (from input files)
- Join groups 
- Quit groups
- Send messages (you can specify the number of groups and time between messages)


# Code1 : 
That code will verify if WhatsApp group exist or no ,after receiving via tkinter window a file that contain information about groups :
- Name
- Url 
<br>
<b>Note</b>: check the excels files for more information
<br><br>
As output you will receive file named output_code1.xlsx  
Output_code1.xlsx is the same input file with new column <b>Work=1 \ DON'T Work=0</b> 

# Code2 : 
If you want to join groups you can use that code
As Code1 will receive 
- Input file via tkinter window but <b>be sure that the file is the output of code1</b> 
- Number of groups to join
<br>
As output you will receive output_code2.xlsx (input file with new column 'Joined=1 \ Otherwis=0')

# Code3 :

If you want to send message to your joined groups<br>
You can simply use that code after specifying 
- The message 
- Number of groups
- Time between messages

As output you will have output_code3.xlsx (new columns 'message_sent')
<br>
# Clean : 
You only need to run that script if you want to send new messages because that script will set <br>
all values of column 'message_sent' as 0.



