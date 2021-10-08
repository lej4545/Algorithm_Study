# def solution(maps):
#     maps = [list(i) for i in maps]
#     answer = 0
#     global width, height, sections, temp_section
#     width = len(maps[0])
#     height = len(maps)
#     sections = []
#     for i in range(height):
#         for j in range(width):
#             temp_section =[]
#             if dfs(i, j, maps) == True:
#                 sections.append(temp_section)
#
#     country_list = {}
#     for section in sections:
#         count
#         for country in section:
#             if country in country_list:
#                 country_list[country] += 1
#             else:
#                 country_list[country] = 1
#
#     return sections
#
# def dfs(x,y, maps):
#     if x <= -1 or x >= height or y <= -1 or y >= width:
#         return False
#     if maps[x][y] != '.':
#         temp_section.append(maps[x][y])
#         maps[x][y] = '.'
#         dfs(x-1, y, maps)
#         dfs(x+1, y, maps)
#         dfs(x, y+1, maps)
#         dfs(x, y-1, maps)
#         return True
#     return False
#
# maps = ["AABCA.QA","AABC..QX","BBBC.Y..",".A...T.A","....EE..",".M.XXEXQ","KL.TBBBQ"]
# maps1 = [".A.B.C.D.E",
#          "A.B.C.D.E.",
#          ".A.B.C.D.E",
#          "A.B.C.D.E."]
#
# print(solution(maps))


# def solution(maps):
#     maps = [list(i) for i in maps]
#     width = len(maps[0])
#     height = len(maps)
#     sections = []
#     for i in range(height):
#         for j in range(width):
#             start_dfs(i, j, maps, sections, width, height)
#     total_section = {}
#     for section in sections:
#         section_info = {}       # 섹션별 나라의 Count 계산
#         for country in section:
#             if country in section_info:
#                 section_info[country] += 1
#             else:
#                 section_info[country] = 1
#         section_info_list = list((sorted(section_info.items(), key=lambda item: (item[1], item[0]), reverse=True)))
#         max_country = section_info_list[0][0]
#         max_num = section_info_list[0][1]
#
#         for section_info in section_info_list:
#             country = section_info[0]
#             num = section_info[1]
#             if max_num > num:
#                 if max_country in total_section:
#                     total_section[max_country] += num
#                 else:
#                     total_section[max_country] = num
#             elif max_num == num:
#                 if country in total_section:
#                     total_section[country] += num
#                 else:
#                     total_section[country] = num
#             else:
#                 print('Error')
#     result = total_section[max(total_section, key=total_section.get)]  # di.get 이용
#     return result
#
# def start_dfs(x, y, maps, sections, width, height):
#     if x <= -1 or x >= height or y <= -1 or y >= width:
#         return False
#     section = []
#     if maps[x][y] != '.':
#         section.append(maps[x][y])
#         maps[x][y] = '.'
#         dfs(x - 1, y, maps, section, width, height)
#         dfs(x + 1, y, maps, section, width, height)
#         dfs(x, y + 1, maps, section, width, height)
#         dfs(x, y - 1, maps, section, width, height)
#         sections.append(section)
#
# def dfs(x,y, maps, section, width, height):
#     if x <= -1 or x >= height or y <= -1 or y >= width:
#         return False
#     if maps[x][y] != '.':
#         section.append(maps[x][y])
#         maps[x][y] = '.'
#         dfs(x-1, y, maps, section, width, height)
#         dfs(x+1, y, maps, section, width, height)
#         dfs(x, y+1, maps, section, width, height)
#         dfs(x, y-1, maps, section, width, height)
#
# maps = ["AABCA.QA","AABC..QX","BBBC.Y..",".A...T.A","....EE..",".M.XXEXQ","KL.TBBBQ"]
# print(solution(maps))
# maps = ["XY..", "YX..", "..YX", ".AXY"]
# print(solution(maps))
# maps = [".A.B.C.D.E",
#          "A.B.C.D.E.",
#          ".A.B.C.D.E",
#          "A.B.C.D.E."]
# print(solution(maps))

## 단지번호 붙이기

