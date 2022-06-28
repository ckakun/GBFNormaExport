# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import csv
import glob

class NormaExport():

    # 本戦ノルマの指定
    NORMA = 400000000
    # 対象HTMLファイルのフォルダ
    HTMLS = ".\ContributionHTMLs\*"
    # 出力先ファイル
    OUTPUT = ".\GBFNorma.tsv"

    def __init__(self):
        # 貢献度HTML一覧の取得
        self.files = glob.glob(self.HTMLS)
        # 変数定義
        self.memberName = []
        self.memberContribution = []
        self.exportData = []

    # メイン処理
    def main(self):
        try:
            # 3ページ分の処理
            for file in self.files:
                # HTML情報取得
                soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")
                # メンバー情報一覧の取得
                memberDetail = soup.find_all('div', class_='prt-member-detail')
                # 貢献度等の取得処理
                self.contributionGetter(memberDetail)
            # 出力データの作成
            self.createExportData()
            # TSVファイルへの出力処理
            self.exportTsv()
        except Exception:
            import traceback
            traceback.print_exc()


    # HTML解析、貢献度・GNの取得
    def contributionGetter(self, memberDetail):
        for member in memberDetail:
            # GNの取得
            for mem in member.find_all('div', class_='prt-member-name'):
                self.memberName.append(mem.find('div', class_='txt-member-name').get_text())
            # 貢献度の取得
            for mem in member.find_all('div', class_='prt-member-point'):
                self.memberContribution.append(mem.find('div', class_='txt-member-value').get_text())

    # 出力用のデータ作成
    def createExportData(self):
        print(len(self.memberName))
        for key in range(len(self.memberName)):
            norma = int(self.memberContribution[key].replace(',', '')) + self.NORMA
            self.exportData.append([self.memberName[key], self.memberContribution[key], '{:,}'.format(norma)])

    # TSVへ出力
    def exportTsv(self):
        header = ['GN', '本戦開始時貢献度', 'ノルマ貢献度']
        f = open(self.OUTPUT, 'w', encoding='utf-8', newline="")
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
        writer.writerows(self.exportData)
        f.close()

if __name__ == '__main__':
    NormaExport = NormaExport()
    NormaExport.main()
