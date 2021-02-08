class Log():

    def readLog(self, filepath):
        checkLogs = open(filepath, 'r')
        recordedId = int(checkLogs.read().strip())
        checkLogs.close()
        return recordedId

    def storeLog(self, filepath, recordedId):
        writeLog = open(filepath, 'w')
        writeLog.write(str(recordedId))
        writeLog.close()
        return