from corpus import Corpus
import pandas as pd
from dateutil.parser import parse
import random
import language_check
from textblob import TextBlob

corpus = Corpus()
templateCorpus = corpus.getTemplateCorpus()
textDictionary = corpus.getTextDictionary()
numericDictionary = corpus.getNumericDictionary()
tool = language_check.LanguageTool('en-US')

def is_date(string, fuzzy=False):
    try: 
        if isinstance(string, str):
            parse(string, fuzzy=fuzzy)
            return True
        elif isinstance(string, pd.Timestamp):
            return True
        else:
            return False
    except ValueError:
        return False

def is_binary(columnNumber):
    values = dataset.iloc[:, columnNumber]
    values = [str(value) for value in values]
    values = [value.lower().strip() for value in values]
    if(all(value in ['yes', 'no'] for value in values) or 
        all(value in ['y', 'n'] for value in values) or 
        all(value in ['true', 'false'] for value in values) or 
        all(value in ['0', '1'] for value in values)): 
            return True
    return False

def getColumnCategory(cellValue, columnHeader):
    words = columnHeader.split()
    if isinstance(cellValue, str):
        if 'date' in columnHeader:
            return 'date'
        for key, value in textDictionary.items():
            for word in words:
                if word.startswith(key):
                    return value
        return 'default_string'
    else:
        for key, value in numericDictionary.items():
            for word in words:
                if word.startswith(key):
                    return value
        return 'default'

def getAllTemplatesFor(col, templateType):
    list_of_lists = []
    with open(col + str(templateType) + '.txt') as f:
        for line in f:
            list_of_lists.append(line)
    return list_of_lists

def getNameWithoutBrackets(string):
    string = str(string)
    return string.replace(string[string.find('('):string.find(')')+1], '').strip()

def getSingular(string):
    blob = TextBlob(string)
    plurals = [word.singularize() for word in blob.words]
    return plurals[0]

def getPlural(string):
    blob = TextBlob(string)
    plurals = [word.pluralize() for word in blob.words]
    return plurals[0]


dataset = pd.read_excel('example04.xls')

head = dataset.columns[0].lower()
head = head.replace("name of ", "")
head = head.replace("names of ", "")
head = head.replace("name for ", "")
head = head.replace("'s names", "")
head = head.replace("'s name", "")
head = head.replace("' names", "")
head = head.replace("' name", "")
head = head.replace(" names", "")
head = head.replace(" name", "")
head = head.replace(" ids", "")
head = head.replace(" id", "")

if (head == 'first') | (head == 'last'):
    head = 'Person'
dataset.rename(columns = {dataset.columns[0] : head}, inplace=True)

for col in dataset.columns:
    dataset.rename(columns = {col : col.replace("the ", "")}, inplace=True)

columnCategories = []
for i in range (len(dataset.columns)):
    if is_date(dataset.iloc[0, i]):
        columnCategories.append('date')
    elif is_binary(i):
        columnCategories.append('binary')
    else:
        columnCategories.append(getColumnCategory(dataset.iloc[0, i], dataset.columns[i].lower()))

questions = []
for columnNumber in range(1, len(columnCategories)):
    columnAnnotation = columnCategories[columnNumber]
    in_unit = dataset.columns[columnNumber][dataset.columns[columnNumber].find('(')+1:dataset.columns[columnNumber].find(')')]
    unit = in_unit.replace('in', '').replace('In', '')
    availableTemplateTypes = templateCorpus.iloc[templateCorpus.loc[templateCorpus['Template_Category'] == columnAnnotation].index[0]]
    columnName = dataset.columns[columnNumber]
    columnNameWithoutBrackets = getNameWithoutBrackets(columnName)
    if availableTemplateTypes['Type_1'] == 1 :
        templates = getAllTemplatesFor(columnAnnotation, 1)
        templates = [template.replace('\n', '') for template in templates]
        template = templates[random.randint(0, len(templates)-1)]
        selectedRowNumber = random.randint(0, len(dataset)-1)
        #use dictionary and for loop to make this code crisp
        template = template.replace("_row_", dataset.iloc[selectedRowNumber, 0]) #remove bracketed terms
        template = template.replace("_col_", columnName)
        template = template.replace("_colwb_", columnNameWithoutBrackets)
        template = template.replace("_unit_", unit)
        template = template.replace("_in-unit_", in_unit)
        template = template.replace("_data_", str(dataset.iloc[selectedRowNumber, columnNumber]))
        template = template.replace("_master-column-header_", dataset.columns[0])
        template = template.replace("_master-column-header-singular_", getSingular(dataset.columns[0]))
        template = template.replace("_master-column-header-plural_", getPlural(dataset.columns[0]))
#        questions.append(language_check.correct(template, tool.check(template)))
        questions.append(template)
        print(template)

    if availableTemplateTypes['Type_2'] == 1 :
        templates = getAllTemplatesFor(columnAnnotation, 2)
        templates = [template.replace('\n', '') for template in templates]
        template = templates[random.randint(0, len(templates)-1)]
        selectedRowNumber = random.randint(0, len(dataset)-1)
        data = str(dataset.iloc[selectedRowNumber, columnNumber])
        #use dictionary and for loop to make this code crisp
        if availableTemplateTypes['Data_Type'] == 'number':
            variation = (max(dataset.iloc[:, columnNumber]) - min(dataset.iloc[:, columnNumber]))*0.2
            template = template.replace("_less_", str(min(dataset.iloc[:, columnNumber])+variation))
            template = template.replace("_more_", str(max(dataset.iloc[:, columnNumber])-variation))
            template = template.replace("_sample_", data[:round(len(data)/2)])
        template = template.replace("_col_", columnName)
        template = template.replace("_colwb_", columnNameWithoutBrackets)
        template = template.replace("_unit_", unit)
        template = template.replace("_unit-in_", in_unit)
        template = template.replace("_master-column-header_", dataset.columns[0])
        template = template.replace("_master-column-header-singular_", getSingular(dataset.columns[0]))
        template = template.replace("_master-column-header-plural_", getPlural(dataset.columns[0]))
 #       questions.append(language_check.correct(template, tool.check(template)))
        questions.append(template)
        print(template)

    if availableTemplateTypes['Type_3'] == 1:
        templates = getAllTemplatesFor(columnAnnotation, 3)
        templates = [template.replace('\n', '') for template in templates]
        template = templates[random.randint(0, len(templates)-1)]
        selectedRowNumbers = random.sample(range(0, len(dataset)-1), 2)
        template = template.replace("_row1_", getNameWithoutBrackets(dataset.iloc[selectedRowNumbers[0], 0]))
        template = template.replace("_row2_", getNameWithoutBrackets(dataset.iloc[selectedRowNumbers[1], 0]))
        template = template.replace("_col_", columnName)
        template = template.replace("_colwb_", columnNameWithoutBrackets)
        template = template.replace("_unit_", unit)
        template = template.replace("_in-unit_", in_unit)
        template = template.replace("_data1_", str(dataset.iloc[selectedRowNumbers[0], columnNumber]))
        template = template.replace("_data2_", str(dataset.iloc[selectedRowNumbers[1], columnNumber]))
        template = template.replace("_master-column-header_", dataset.columns[0])
        template = template.replace("_master-column-header-singular_", getSingular(dataset.columns[0]))
        template = template.replace("_master-column-header-plural_", getPlural(dataset.columns[0]))
#        questions.append(language_check.correct(template, tool.check(template)))
        questions.append(template)
        print(template)

del i, head, col
del columnName, columnNumber, columnAnnotation, columnNameWithoutBrackets
del availableTemplateTypes, unit, in_unit, template, templates 
del variation, selectedRowNumber, selectedRowNumbers, data
