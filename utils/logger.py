
class Logger:
    begin = 0
    log_file_name = 'dbg_report.txt'

    @staticmethod
    def log(msg):
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
