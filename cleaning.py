import re
from ip_rotate import check_ip_rotation

def get_data_href():
    pattern = r"data-href=['\"]([^'\"]+)['\"]"
    respp = check_ip_rotation()
    final_href_list = re.findall(pattern, respp["internship_list_html"])
    return final_href_list

