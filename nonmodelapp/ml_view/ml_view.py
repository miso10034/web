### 데이터 처리 라이브러리 불러들이기
import pandas as pd

### 데이터셋 분류 라이브러리(전처리 라이브러리)
from sklearn.model_selection import train_test_split

### 사용할 훈련모델 불러들이기
from sklearn.linear_model import LogisticRegression

### 훈련모델 저장 및 로드하는 라이브러리
import joblib

class ML_View : 

    ### 클래스 생성시 함수 호출해 실행시키기
    def __init__(self):
        self.initDataFrame()
        self.data_preprocess()
        self.modelCreate()
        self.modelFit()
        self.modelSave()

        # 예측하기
        self.modelLoad()

    ### 데이터 읽어 들이기
    def initDataFrame(self):
        ### 생선분류데이터.csv 파일 읽어들이기
        # - 데이터프레임 변수명 : fish
        file_path = "./nonmodelapp/ml_view/05_생선_분류_데이터셋.csv"
        self.fish = pd.read_csv(file_path)

    ### 데이터 전처리
    def data_preprocess(self):
        ### 독립변수와 종속변수로 분리하기(전처리 : 데이터 정제 처리)
        # - 독립변수(특성) : fish_input 변수 사용 (Species를 제외한 모든 것)
        # - 종속변수() : fish_target 변수 사용 (Species 컬럼)

        fish_input = self.fish[['Weight','Length','Diagonal',
                                'Height','Width']].to_numpy() # 2차원
        fish_target = self.fish['Species'].to_numpy() # 1차원

        ### 데이터 분류하기
        # 분류1 : 훈련(70) : 테스트(30)
        # 분류2 : 훈련(60) : 검증(20) : 테스트(20)

        self.train_input, self.test_input, self.train_target, self.test_target = train_test_split(fish_input,
                                                                                        fish_target,
                                                                                        test_size = 0.3,
                                                                                        random_state=42)

    ### 모델 생성하기
    def modelCreate(self) :
        ### 모델 생성하기
        # - 훈련 횟수 : max_iter
        self.lr = LogisticRegression(max_iter = 20000)

    ### 모델 훈련시키기
    def modelFit(self) :
        ### 훈련모델 훈련시키기
        # - 훈련데이터 : train 데이터 사용
        self.lr.fit(self.train_input, self.train_target)

    ### 훈련모델 저장시키기
    def modelSave(self) :
        ### 훈련모델 저장하기
        joblib.dump(self.lr, "./nonmodelapp/ml_view/model/LR_Fish_model.pkl")

    ### 훈련모델 불러오기
    def modelLoad(self) :
        ### 훈련모델 로드하기
        self.load_model = joblib.load("./nonmodelapp/ml_view/model/LR_Fish_model.pkl")

    ### 훈련모델 정확도(평가) 확인 : 
    def getModelScore(self) :
        ### 정확도 검증하기 : 
        score = self.load_model.score(self.test_input,
                                            self.test_target)
        return score
    
    ### 예측 하기 
    def getModelPredict(self, random_data) : 
        ### 예측(분류)하기
        pred_data = self.load_model.predict(random_data)
        return pred_data