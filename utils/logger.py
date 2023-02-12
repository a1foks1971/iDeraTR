from datetime import datetime
class Logger:
    begin = 0
    log_file_name = 'dbg_report.txt'

    @staticmethod
    def add_time_to_message(msg):
        # "https://www.programiz.com/python-programming/datetime/strftime"
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f    ")
        return  current_time + msg

    @staticmethod
    def log(in_msg):
        msg = Logger.add_time_to_message(in_msg)
        print(msg)
        # write_to_file(msg)
        if 0 == Logger.begin :
            f = open(Logger.log_file_name, 'w')
            f.write(msg + '\n')
            Logger.begin = 1
            f.close()
        else:
            f = open(Logger.log_file_name, 'a')
            f.write(msg + '\n')
