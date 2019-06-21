import re

def extract_error(input_file):
    print(input_file)
    output_file = open("output_file.txt","w+")
    for i in input_file:
        if(re.match(r'^ERROR',i) or re.match(r'^WARNING',i)):
            output_file.write(i)
    output_file.close()
   
if __name__ == '__main__':
    #input_file = ['DEBUG:root:debug', 'INFO:root:info', 'Warning:root:warning', 'ERROR:root:error', 'CRITICAL:root:critical']
    input_file = open("error_log_input.txt","r")
    extract_error(input_file)
    input_file.close()
    output_file = open("output_file.txt","r")
    if(output_file):
        for i in output_file:
            print(i)
    else:
        print("No errors found")