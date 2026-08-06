class Logger:
    __instance=None
    def __new__(cls,file_name:str):
        if cls.__instance==None:
            cls.__instance=super().__new__(cls)
            cls.__instance.file_name=file_name
            cls.__instance.log_count=0
            return cls.__instance
        else:
            return cls.__instance

    def log(self,message):
        print(f"Logging in message:: {message} ::in {self.file_name}",self.log_count)
        self.log_count+=1

    def get_log_count(self):
        return self.log_count

log1=Logger("abc")
print(f"log1 {log1},id:{id(log1)}")

log2=Logger("abc")
print(f"log2 {log2},id:{id(log2)}")
log3=Logger("abc")
print(f"log3 {log3},id:{id(log3)}")

log1.log("this islog one")
log2.log("this is the log two")
log3.log("this islog three")
log1.log("this islog one again")
print(log1.get_log_count())
print(log2.get_log_count())
