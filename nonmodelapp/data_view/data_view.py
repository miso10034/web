## 나만의 라이브러리 만들기
### 시각화 라이브러리 불러들이기
import seaborn as sns
import matplotlib.pyplot as plt

class Data_View : 

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) : 
        self.initDataFrame()
        self.data_preprocess()
        self.initVisualization()
        self.saveFig()

    ### 엠스콤 데이터프레임으로 읽어들이기
    def initDataFrame(self) : 
        self.ans = sns.load_dataset("anscombe")

    
    ### 데이터 전처리
    def data_preprocess(self) : 
        self.data1 = self.ans[self.ans['dataset'] == "I"]
        self.data2 = self.ans[self.ans['dataset'] == "II"]
        self.data3 = self.ans[self.ans['dataset'] == "III"]
        self.data4 = self.ans[self.ans['dataset'] == "IV"]


    ### 그래프 그리기
    def initVisualization(self) :
        ### 하나의 그래프에 4개의 각 그래프 표현하기

        # 하나의 그래프 객체 선언
        self.fig = plt.figure()

        ### 4개의 그래프가 들어갈 공간 만들기
        # - add_subplot(행, 열, 위치)
        ax1 = self.fig.add_subplot(2, 2, 1)
        ax2 = self.fig.add_subplot(2, 2, 2)
        ax3 = self.fig.add_subplot(2, 2, 3)
        ax4 = self.fig.add_subplot(2, 2, 4)

        ### 각 공간 그래프에 제목 달기
        ax1.set_title("data1")
        ax2.set_title("data2")
        ax3.set_title("data3")
        ax4.set_title("data4")

        ### 그래프에 데이터 넣어서 그리기
        ax1.plot(self.data1["x"], self.data1["y"], "o", c="b")
        ax2.plot(self.data2["x"], self.data2["y"], "o", c="r")
        ax3.plot(self.data3["x"], self.data3["y"], "o", c="g")
        ax4.plot(self.data4["x"], self.data4["y"], "o", c="y")

        ### 그래프 전체 제목 넣기
        self.fig.suptitle("Anscombe Data")

        ### 그래프 겹치지 않게 정렬하기
        self.fig.tight_layout()

    
    ### 그래프 저장하기
    def saveFig(self) :
        self.fig.savefig("./nonmodelapp/static/nonmodelapp/data_img/fig.png")