# imports
import pandas as pd
import logging
import keyword_library as keyword

testscript_excel_path = r'C:\\Users\\athangaraj001\\PycharmProjects\\ADAPT_Python\\sampledata.xlsx'
LOGGER = logging.getLogger(__name__)


def convert_to_dict(filepath, sheetname, index_column):
    df_excel_sheet = pd.read_excel(filepath, sheetname, index_col=index_column)
    dict_excel_sheet = df_excel_sheet.to_dict()
    return dict_excel_sheet


def convert_to_df(filepath, sheetname):
    df_excel_sheet = pd.read_excel(filepath, sheetname)
    return df_excel_sheet


def absorb_data():
    df_scenario_manager = convert_to_df(testscript_excel_path, 'scenario_manager')
    LOGGER.info(df_scenario_manager)
    df_testcase_manager = convert_to_df(testscript_excel_path, 'testcase_manager')
    df_teststep_manager = convert_to_df(testscript_excel_path, 'teststep_manager')
    list_sc = df_scenario_manager['sc_no'].tolist()

    for every_sc in list_sc:
        df_testcases = df_testcase_manager.loc[df_testcase_manager['sc_no'] == every_sc]
        list_tcs = df_testcases['tc_no'].tolist()

        for every_tc in list_tcs:
            df_teststeps = df_teststep_manager.loc[df_teststep_manager['tc_no'] == every_tc]
            # list_tstps = df_teststeps['ts_no'].tolist()
            list_keywords = df_teststeps['keyword'].tolist()
            for every_keyword in list_keywords:
                LOGGER.info('** executing keyword - ' + every_keyword + ' **')
                exec("result = keyword." + every_keyword + '()')


def sf_login():
    print('sf login')











