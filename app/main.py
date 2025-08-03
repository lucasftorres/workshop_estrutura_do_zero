from pipeline.extract import extract_from_excel
from pipeline.transform import concat_data_frames
from pipeline.load import load_excel

if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    data_frame = concat_data_frames(data_frame_list)
    load_excel(data_frame, 'data/output', 'output')
# listas_de_data_frame = extract_from_excel('C:/Users/Lucas/Documents/jornada_projects/workshop_estrutura_do_zero/data/input')
# print(listas_de_data_frame)