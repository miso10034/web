### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd

### 지도 시각화 라이브러리 불러들이기
import folium

class Map_View : 

    ## 1번 2번 3번이 모두 실행이 되어야 getMap 이 실행이 된다.
    ### 클래스 생성시 아래 함수 모두 실행시키기
    # - 생성자에서 호출
    def __init__(self) :
        self.initDataFrame()
        self.map_base()
        self.map_location()

    
    # 1번
    ### 데이터 읽어들이기
    def initDataFrame(self) :
        ### 4_4 엑셀 데이터셋 읽어들이기
        # - 데이터프레임 변수명 : seoul_starbucks
        file_path = "./nonmodelapp/map_view/4_4_seoul_starbucks_list.xlsx"
        self.seoul_starbucks = pd.read_excel(file_path)
    
    # 2번
    ### 지도맵 그리기
    def map_base(self) :
        self.starbucks_map2 = folium.Map(
            ### 최초에 보여줄 지도위치(위/경도) 지정 
            # - 최초에 중심점을 기준으로 지도가 그려짐
            location = [37.573050, 126.979189],

            ### 지도 스타일 지정하기
            # - 도시형 건물, 산림, 하천/도로 등 스타일 지정
            # openstreetmap : 도시형 건물 스타일(가장 일반적으로 사용됨)
            tiles = "openstreetmap",

            ### 최초에 화면에 보여질 스케일(zoom) 지정하기
            zoom_start = 11,
            ### 너비 지정
            width = "100%",

            ### 높이 지정
            height = "100%"
        )

    # 3번
    ### 스타벅스 타입별 매장위치 표시하기
    def map_location(self) : 
        for idx in self.seoul_starbucks.index : 
            ### 위경도 데이터 추출하기
            lat = self.seoul_starbucks.loc[idx, "위도"]
            lng = self.seoul_starbucks.loc[idx, "경도"]
            store_type = self.seoul_starbucks.loc[idx, "매장타입"]

            fillcolor = ""
            size = 1

            if store_type == 'general':
                fillcolor = "gray"
                size = "3"
            elif store_type == 'reserve':
                fillcolor = "blue"
                size = "5"
            elif store_type == 'generalDT':
                fillcolor = "red"
                size = "5"

            ### 지도에 마커 표시하기
            # - 마커 스타일 지정하기
            # - CircleMarker : 원모양 마커
            folium.CircleMarker(
            # 마커 위치 지정
            location = [lat, lng],
            #마커 채우기 색상
            fill_color = fillcolor,
            fill = True,
            # 마커 테두리 색상
            color = "red",
            # 마커 투명도
            fill_opacity = 1,
            # 마커 테두리 사이즈
            weight = 1,
            # 마커 원의 크기 
            radius = size
            ).add_to(self.starbucks_map2) 

    ## 정의는 끝
    ## 최종결과값인 self.starbucks_map2를 받아오기


    ### 최종 맵 리턴하기
    def getMap(self) :

        ### starbucks_map2는 html에서 읽어들일수 있는 형식이 아님
        ### 형식 변환이 필요 (지도 코드 -> html 코드로 변환해주는 함수 : _repr_html())
        # - _repr_html() : html 코드로 변환해 줍니다.
        return self.starbucks_map2._repr_html_()

    ### 데이터프레임 리턴하기
    def getDataFrame(self) :
        return self.seoul_starbucks