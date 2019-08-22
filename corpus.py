import pandas as pd
class Corpus:
    def getTemplateCorpus(_self_):
        templateCorpus = [['date', 'date', 1, 1, 0],
                        ['binary', 'binary', 1, 1, 0],
                        ['default', 'string', 1, 0, 0],
                        ['year', 'number', 1, 1, 0],
                        ['age', 'number', 1, 1, 1],
                        ['height', 'number', 1, 1, 1],
                        ['weight', 'number', 1, 1, 1],
                        ['length', 'number', 1, 1, 1],
                        ['ID', 'number', 1, 1, 0],
                        ['percentage', 'number', 1, 1, 1],
                        ['phone_number', 'number', 1, 1, 0],
                        ['pincode', 'number', 1, 1, 0],
                        ['rating', 'number', 1, 1, 1],
                        ['score', 'number', 1, 1, 1],
                        ['size', 'number', 1, 1, 1],
                        ['temperature', 'number', 1, 1, 1],
                        ['simple', 'number', 1, 1, 0],
                        ['money', 'number', 1, 1, 1],
                        ['fraction', 'number', 1, 1, 1],
                        ['measure', 'number', 1, 1, 1],
                        ['default_string', 'string', 1, 1, 0],
                        ['code', 'string', 1, 1, 0],
                        ['person', 'string', 1, 1, 0],
                        ['organisation', 'string', 1, 1, 0],
                        ['process', 'string', 1, 1, 0],
                        ['location', 'string', 1, 1, 0],
                        ['blood_group', 'string', 1, 1, 0],
                        ['language', 'string', 1, 1, 0],
                        ['nationality', 'string', 1, 1, 0],
                        ['river', 'string', 1, 1, 0],
                        ['sports', 'string', 1, 1, 0]]

        templateCorpus = pd.DataFrame(templateCorpus, columns = ['Template_Category', 'Data_Type', 'Type_1', 'Type_2', 'Type_3']) 
        return templateCorpus
    
    def getNumericDictionary(_self_):
        numericDictionary = {'number of': 'simple',
                            'no. of': 'simple',
                            'fax': 'phone_number',
                            'pager': 'phone_number',
                            'mobile': 'phone_number',
                            'contact': 'phone_number',
                            'phone': 'phone_number',
                            'dial': 'phone_number',
                            'number': 'default',
                            'no.': 'default',
                            'height': 'height',
                            'ht.': 'height',
                            'elevation': 'height',
                            'weight': 'weight',
                            'wt.': 'weight',
                            'mass': 'weight',
                            'length': 'length',
                            'width': 'length',
                            'breadth': 'length',
                            'depth': 'length',
                            'diameter': 'length',
                            'radius': 'length',
                            'perimeter': 'length',
                            'pincode': 'pincode',
                            'zipcode': 'pincode',
                            'code': 'ID',
                            'ssn': 'ID',
                            'imei': 'ID',
                            'uid': 'ID',
                            'imsi': 'ID',
                            'percent': 'percentage',
                            '%': 'percentage',
                            'grade': 'rating',
                            'scale': 'rating',
                            'rating': 'rating',
                            'level': 'rating',
                            'score': 'score',
                            'mark': 'score',
                            'result': 'score',
                            'tally': 'score',
                            'byte': 'size',
                            'kb': 'size',
                            'mb': 'size',
                            'gb': 'size',
                            'tb': 'size',
                            'bit': 'size',
                            'nibble': 'size',
                            'word': 'size',
                            'temperature': 'temperature',
                            'melting point': 'temperature',
                            'melting pt': 'temperature',
                            'boiling point': 'temperature',
                            'boiling pt': 'temperature',
                            'freezing point': 'temperature',
                            'freezing pt': 'temperature',
                            'evaporation point': 'temperature',
                            'evaporation pt': 'temperature',
                            'value': 'simple',
                            'unit': 'simple',
                            'volume': 'simple',
                            'size': 'simple',
                            'money': 'money',
                            'capital': 'money',
                            'amount': 'money',
                            'salary': 'money',
                            'fund': 'money',
                            'revenue': 'money',
                            'interest': 'money',
                            'price': 'money',
                            'cost': 'money',
                            'earning': 'money',
                            'principle': 'money',
                            'income': 'money',
                            'emi': 'money',
                            'rupee': 'money',
                            'usd': 'money',
                            'euro': 'money',
                            'dollar': 'money',
                            'dinar': 'money',
                            'rs.': 'money',
                            '$': 'money',
                            'check': 'money',
                            'fund': 'money',
                            'payment': 'money',
                            'cheque': 'money',
                            'wage': 'money',
                            'expense': 'money',
                            'expenditure': 'money',
                            'fraction': 'fraction',
                            'portion': 'fraction',
                            'ratio': 'fraction',
                            'area': 'measure',
                            'density': 'measure',
                            'population': 'measure',
                            'mean': 'measure',
                            'average': 'measure',
                            'frequency': 'measure',
                            'standard deviation': 'measure',
                            'variance': 'measure',
                            'measure': 'measure',
                            'quota': 'measure',
                            'angle': 'measure',
                            'cubic': 'measure',
                            'square': 'measure',
                            'haemoglobin': 'measure',
                            'hb': 'measure',
                            'bmi': 'measure',
                            'body mass index': 'measure',
                            'age': 'age',
                            'id': 'ID',
                            'mis': 'ID',
                            'total': 'simple',
                            'year': 'year',
                            'yr': 'year',
                            'annum': 'year'} 
        return numericDictionary

    def getTextDictionary(_self_):
        textDictionary = {'code': 'code',
                        'pan': 'code',
                        'artist': 'person',
                        'dr.': 'person',
                        'doctor': 'person',
                        'player': 'person',
                        'person': 'person',
                        'prof': 'person',
                        'student': 'person',
                        'employee': 'person',
                        'manager': 'person',
                        'ceo': 'person',
                        'md': 'person',
                        'child': 'person',
                        'teacher': 'person',
                        'principal': 'person',
                        'president': 'person',
                        'mayor': 'person',
                        'man': 'person',
                        'boy': 'person',
                        'girl': 'person',
                        'architect': 'person',
                        'minister': 'person',
                        'father': 'person',
                        'mother': 'person',
                        'dentist': 'person',
                        'nurse': 'person',
                        'lawyer': 'person',
                        'accountant': 'person',
                        'psychologist': 'person',
                        'engineer': 'person',
                        'librarian': 'person',
                        'statistician': 'person',
                        'officer': 'person',
                        'scientist': 'person',
                        'designer': 'person',
                        'developer': 'person',
                        'captain': 'person',
                        'judge': 'person',
                        'prosecutor': 'person',
                        'therapist': 'person',
                        'husband': 'person',
                        'wife': 'person',
                        'spouse': 'person',
                        'daughter': 'person',
                        'organisation': 'organisation',
                        'organization': 'organisation',
                        'company': 'organisation',
                        'hospital': 'organisation',
                        'brand': 'organisation',
                        'school': 'organisation',
                        'party': 'organisation',
                        'institution': 'organisation',
                        'agency': 'organisation',
                        'league': 'organisation',
                        'club': 'organisation',
                        'association': 'organisation',
                        'college': 'organisation',
                        'university': 'organisation',
                        'kindergarten': 'organisation',
                        'department': 'organisation',
                        'prison': 'organisation',
                        'jail': 'organisation',
                        'asylum': 'organisation',
                        'station': 'organisation',
                        'process': 'process',
                        'technique': 'process',
                        'method': 'process',
                        'treatment': 'process',
                        'procedure': 'process',
                        'protocol': 'process',
                        'framework': 'process',
                        'mechanism': 'process',
                        'operation': 'process',
                        'practice': 'process',
                        'system': 'process',
                        'airport': 'location',
                        'city': 'location',
                        'country': 'location',
                        'location': 'location',
                        'capital': 'location',
                        'address': 'location',
                        'colony': 'location',
                        'neighbourhood': 'location',
                        'locate': 'location',
                        'district': 'location',
                        'county': 'location',
                        'state': 'location',
                        'province': 'location',
                        'continent': 'location',
                        'hemisphere': 'location',
                        'region': 'location',
                        'venue': 'location',
                        'spot': 'location',
                        'place': 'location',
                        'blood group': 'blood_group',
                        'language': 'language',
                        'dialect': 'language',
                        'speech': 'language',
                        'jargon': 'language',
                        'vocab': 'language',
                        'nationality': 'nationality',
                        'citizenship': 'nationality',
                        'ethnicity': 'nationality',
                        'river': 'river',
                        'tributary': 'river',
                        'estuary': 'river',
                        'stream': 'river',
                        'sport': 'sports',
                        'athletic': 'sports',
                        'game': 'sports'}   
        return textDictionary
