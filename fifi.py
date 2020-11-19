import os
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from konlpy.tag import Okt
import numpy as np
import pandas as pd
import joblib
from bs4 import BeautifulSoup
import requests
import jpype

metrix = pd.read_csv('end_game.csv', index_col = 0)

okt = Okt()
model = joblib.load('project_ppt.pkl')

def tw_tokenizer(text):
    tokens_ko = okt.morphs(text)
    return tokens_ko

Tfidf_vect = TfidfVectorizer(tokenizer = tw_tokenizer ,
                             max_df = 0.9,
                             min_df = 0
                            )

Tfidf_vect_morphs = Tfidf_vect.fit_transform(metrix['comment'])

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    if jpype.isJVMStarted():
        jpype.attachThreadToJVM()
    
    x = request.form['left']
    qus = model.predict(Tfidf_vect.transform([x]))
    
    
    if int(qus) == 1:
        if x.find('동아리') >= 0:
            return '우리학교 동아리에는 더씨(밴드), 스콥스(대중가요), 시내터(모던락), 아르니아(클래식기타), 메이화(치어리딩), 올클리어(춤), 외침 플로우데블러(힙합), 산악부(등산), 아타락시아(만화), Filos(스키), 한아름(사진), GG(게임), 굿네이버스 로타랙트 사랑의손 젊은 새 이웃 Won(봉사), 한반도(역사기행), 레드맥스(증권투자), 사회복지연구회(학술), 코아시스(학술), 타키온즈(야구), 파닥파닥(배드민턴), 햇귀(탁구), K.S.C(축구), SNAP(농구부), 에코 예수전도단 한국기독학생회(종교), CCC(찬양) 등이 있어요!,'
        elif x.find('졸업조건')>= 0 or x.find('졸업요건') >= 0:
            return '에브리타임 인공지능 봇이에요! 우리학교 졸업조건 입니다! - 1.8학기 이상 등록한 자(다만, 조기졸업대상자는 예외)  2.학 점 : 130학점(2012 이전 입학자 140학점) 이상 취득  3.교과목 이수 : 각 학부(과)에 규정된 기초과목(학부기초, 전공기초), 전공과목(전공필수, 전공선택), 교양필수(기초교양), 교양선택(균형교양, 계열교양), 자유선택  4.졸업종합평가 : 합격   5.채 플 : 4회 이상 통과. 단, 편입생은 2회 이상 통과'
        elif x.find('증명서') >=0:
            return '본교 방문신청 : 증명서자동발급기(샬롬관1층), 교학행정실(샬롬관1층, 경천관1층), 교무팀(본관1층) - FAX 민원신청 : 가까운 행정기관(주민센터, 시, 군, 구청 ,읍, 면)에서 FAX민원 신청 → G4C로 신청된 민원 접수 → 신청 증명서를 행정기관으로     FAX 송부 (전산으로 자동 송부)- 온라인 발급 : 학교 홈페이지-자주 찾는 서비스- 인터넷 증명발급에서 신청 후 개인용 프린터로 출력'
        elif x.find('성적장학금') >= 0 or x.find('장학금') >=0:
            return '학점(2012년 이전 입학자 18학점) 이상 취득 및 평점평균 3.0이상 - 학부/과 학년별 상위 10%선발 - 재학인원 15명 미만 학년수석 없음 - 재학인원 5명 미만 장학생 배정 없음- 4학년은 12학점이지만 후기졸업(8월)자는 아래 학점취득 기준 적용 - 학년수석 : 수업료 67% 감면 - 학년우수 : 수업료 47% 감면- 취득학점수가 많은 자→직전학기 평점평균 우수자→연소자→입학년도가 빠른자'
        elif x.find('행정반') >=0:
            return '행정반 번호가 있는 주소입니다. https://web.kangnam.ac.kr/menu/d32b0ae4b98a62cad835c588275d3407.do'
        elif x.find('달구지') >=0:
            return '운행노선(08:10~19:15 : 이공관 -> 인문사회관 -> 학교 앞4거리 -> 기흥역 -> 강남대역 -> 샬롬관 -> 본관 -> 이공관 / 달구지 타고 내려가는 법 : 이공관 -> 인문사회관 -> 강남대 상가 건물(빠아앙 앞, 버스정류장 옆) -> 기흥역 참고 게시글 - https://everytime.kr/389202/v/100973908 '
        elif x.find('휴학신청') >=0 or x.find('휴학')>=0:
            return '신입생, 편입생, 재입학생은 입학한 첫 학기에는 일반휴학을 할 수 없습니다. 단, 아래의 경우에는 입학 첫 학기에도 휴학을 신청할 수 있습니다. 일반휴학은 재학 중 3회를 초과할 수 없습니다. 입대휴학, 임신·출산휴학, 육아휴학, 창업휴학은 일반휴학 횟수에 포함되지 않습니다. 신청은 학교 홈페이지 > 종합정보시스템 접속 > 학적변동관리 > 일반휴학신청 > 신규휴학신청 클릭'
        elif x.find('미용실') >= 0:
            return '개발자의 추천픽! https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8B%AC%EB%82%98%EB%9D%BC+%EB%AF%B8%EC%9E%A5'
        elif x.find('학생증') >=0:
            return '안녕하세요. 에브리타임 인공지능 봇이에요! 학생증 발급 안내는 https://web.kangnam.ac.kr/menu/board/info/e4058249224f49ab163131ce104214fb.do?encMenuSeq=1056addfbd6d939580620e461b59b641&encMenuBoardSeq=fa412d9b8d3a11d9c88c29d90913b3f8'
        elif x.find('카페') >=0:
            return '학교안에 카페는 천은관 지하, 샬롬관 지하에 있고, 학교밖에 카페는 매우 많은데 공부하기 좋은곳은 에이어바웃 입니다!'
        elif x.find('힐링존') >=0:
            return '강남대 힐링존은 천은관, 경천관, 샬롬관, 인사관에 있습니다!'
        elif x.find('열람실')>=0:
            return '학기중 강남대 제1 제2 열람실은 06~23시(시험기간 24시간, 칸막이 있음, 노트북 사용가능) / 제3 열람실은 24시간(칸막이 있음) / 전자정보실 08~20:30 입니다.'
        elif x.find('와이파이')>=0 or x.find('wifi') >=0 or x.find('WIFI') >=0:
            return '강남대학교 와이파이 비밀번호 : officenet1 입니다! (기숙사 포함)'
        elif x.find('pc방') >= 0 or x.find('피방') >=0 or x.find('피시방')>=0:
            return '학교 앞 pc방은 라이또 pc방이 좋아요! '
        else :
            return '모르겠어요.. 전 생각보다 똑똑하지 않아요 ㅠㅠ'
            
                        
    elif int(qus) == 2:
        return '교양 관련 질문인가요?'
    elif int(qus) == 3:
        return '필수교양 관련 질문인가요?'
    elif int(qus) == 4:
        return '경영관리대학 관련 질문인가요? https://bam.kangnam.ac.kr/'
    elif int(qus) == 5:
        return '복지융합대학 관련 질문인가요? https://wc.kangnam.ac.kr/'
    elif int(qus) == 6:
        return '글로벌인재대학 관련 질문인가요? https://gt.kangnam.ac.kr/'
    elif int(qus) == 7:
        return 'ict건설공과대학 관련 질문인가요? https://iwc.kangnam.ac.kr/'
    elif int(qus) == 8:
        return '사범대학 관련 질문인가요? https://knedu.kangnam.ac.kr/'
    
    elif int(qus) == 0:
        if x.find('안녕') >= 0  or x.find('반가워') >= 0:
            return '안녕하세요! 강남대학교에 관한 질문을 입력해주세요.      예)우리학교 와이파이 비번이 뭐야? 오늘 날씨는 어때?'
        elif x.find('날씨') >= 0:
            html = requests.get('https://search.naver.com/search.naver?query=날씨')
            soup = BeautifulSoup(html.text, 'html.parser')
            data1 = soup.find('div', {'class': 'weather_box'})
            
            find_address = data1.find('span', {'class':'btn_select'}).text
            wi = '현재 위치 : '+find_address
        
            find_weather = data1.find('p',{'class': 'cast_txt'}).text
            d = '현재 날씨정보 : ' + find_weather
        

            find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
            wa = '현재 온도 : '+find_currenttemp

            data2 = data1.findAll('dd')
            find_dust = data2[0].find('span', {'class':'num'}).text
            find_ultra_dust = data2[1].find('span', {'class':'num'}).text
            find_ozone = data2[2].find('span', {'class':'num'}).text
            wb = '현재 미세먼지: '+find_dust
            wc = '현재 초미세먼지: '+find_ultra_dust
        
            return wi + ' / ' + d + ' / ' + wb + ' / ' + wc + ' / ' + wa
        
        else :
            return '질문이 아닌 것 같아요.'

    else:
        return '질문이 아닌 것 같아요.'


@app.route('/multiply', methods=['POST'])
def multiply():
    left = request.form['left']
    rite = request.form['rite']

    return str(int(left) * int(rite))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
