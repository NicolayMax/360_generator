import random
import xlsxwriter

forms = 1000
estimators = 100


def getRandomUser():
    return personIds[random.randint(0, forms - 1)]


def getAssesmentPersons(personId, count):
    result = set()
    while len(result) < count:
        p = getRandomUser();
        if (personId != p):
            result.add(p)
    return list(result)


personFile = open("/Users/nikolaj/Downloads/UserPersonID.txt")
result = []
personIds = []

for i in range(0, forms):
    personIds.append(personFile.readline().replace("\n", ""))

personFile.close()

for person in personIds:
    assessmentPersons = getAssesmentPersons(person, estimators)
    # result.append([person, person, "1"])

    # for i in range(70):
    #     result.append([person, assessmentPersons[i], "2"])

    for i in range(0, estimators):
        result.append([person, assessmentPersons[i], "3"])

delimiter = 1
for number in range(delimiter):
    workbook = xlsxwriter.Workbook('/Users/nikolaj/Downloads/out_' + str(number) + '.xlsx')
    worksheet = workbook.add_worksheet("Estimators")
    page_size = round(len(result) / delimiter)
    for index in range(page_size):
        worksheet.write(index, 0, result[index + (number * page_size)][0])
        worksheet.write(index, 1, result[index + (number * page_size)][1])
        worksheet.write(index, 2, int(result[index + (number * page_size)][2]))
    workbook.close()