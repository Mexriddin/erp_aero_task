import json
from typing import List
from additional_task import *


def convert_table_to_json(table, websocket_response, base_ws):
    result = {base_ws['Columns View']: [],
              base_ws['Sort By']: {},
              base_ws['Condition']: {},
              base_ws['Lines per page']: '',
              base_ws['Row Height']: '',
              base_ws['Highlight By']: {},
              'module': 'SO'}

    for i, column in enumerate(table):
        column_name = column["Columns View"]
        if column_name in websocket_response:
            ws_data = websocket_response[column_name]
            index_column = ws_data["index"]
            filter_column = ws_data["filter"]

            # columns
            result['columns'].append({'index': index_column, 'sort': i})

            # order_by
            if column["Sort By"]:
                result['order_by']['direction'] = column["Sort By"],
                result['order_by']['index'] = index_column

            # conditions_data
            conditions_str = column["Condition"]
            conditions = get_conditions_list(conditions_str=conditions_str)
            if conditions:
                result['conditions_data'][filter_column] = conditions

            # page_size
            if column["Lines per page"]:
                result['page_size'] = column["Lines per page"]

            # row_height
            if column["Row Height"]:
                result['row_height'] = column["Row Height"]

            # color_conditions
            color_conditions_str = column["Highlight By"]
            color_conditions = get_highlight_by_list(color_conditions_str)
            if color_conditions:
                result['color_conditions'][index_column] = color_conditions
    return json.dumps(result, indent=4)


def get_conditions_list(conditions_str: str) -> List:
    # Parse condition string on the list
    conditions = []
    if conditions_str:
        for condition in conditions_str.split(","):
            if "=" in condition:
                condition_type, value = condition.split("=")
                conditions.append({'type': condition_type, 'value': value})
    return conditions


def get_highlight_by_list(highlight_by_list_str: str) -> List:
    # Parse highlight string on the list
    highlight_by = []
    high_light_list = []
    if highlight_by_list_str:
        delimiter = highlight_by_list_str.find(")")
        if delimiter > 0:
            high_light_list.append(highlight_by_list_str[:delimiter + 1])
            high_light_list.append(highlight_by_list_str[delimiter + 2:])
        else:
            high_light_list.extend(highlight_by_list_str.split(","))

    for high_light in high_light_list:
        parts = high_light.split("=")
        if len(parts) == 2:
            highlight_type, value = parts
            highlight_by.append({"type": highlight_type, "value": value, "color": ""})
        elif len(parts) == 3:
            highlight_type, value, rgba = parts
            highlight_by.append({"type": highlight_type, "value": value, "color": rgba})
    return highlight_by


print(convert_table_to_json(table=table, websocket_response=websocket_response, base_ws=base_ws))

