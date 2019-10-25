# univ-scraping-remake

## リファレンス  
<https://docs.djangoproject.com/ja/2.2/intro/tutorial01/>

## 使い方  
- 組織の作成
  1. 登録フォームより任意のIDを登録、作成
- 組織への参加
  1. 参加する組織のID、本人の学籍番号、パスワード(ToyoNet-G)を入力  

## 仕様

  **データべース構造**
```
table test(id char primary key,
team_id integer,
class integer);

# 外部キー
table test2(
team_id char primary key,
password integer,
foreign key (team_id) references test(team_id));
```
**API設計**
```
exportData = {"Spring":
               {"Monday":
                 [
                   (x時限目, 講義の有無, クォーター判定),
                   (1~6, 0:無 1:有, 0:1Q|3Q 1:2Q|4Q 2:両方あり),
                 ],
                "Tuesday":...
               },
             "Autumn":
             }
```
