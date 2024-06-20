import pandas as pd

def readData(file):
    data = pd.read_csv(file)
    return data

def rowToDict(data) -> list[dict]:
    data = data.fillna('None')
    dataDict = data.to_dict('records')
    return dataDict

def main():
    file = 'forminfo.csv'
    data = readData(file)
    # print(data)
    print(data.columns)
    data = rowToDict(data)
    print(data[0])
    print(data[0]['1st Email'])
if __name__ == '__main__':
    main()