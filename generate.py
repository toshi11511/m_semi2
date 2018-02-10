#!/usr/bin/python3
# -*- coding: utf-8 -*-

# モジュールのインポート
import sys
import cgitb
import glob
import re
import codecs

sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")

print("***HTML_GENERATOR***")
File_Format = "format/format.txt"
txtlist = glob.glob("*.txt")
# glob()関数でファイル検索（ワイルドカードパターンマッチングが可能）
for infile in txtlist:
    # f1 = codecs.open(infile, "r", encoding="utf-8-sig")
    # BOMで引っかかるのでcodecsモジュールでutf-8-sig
    with codecs.open(infile, "r", encoding="utf-8-sig") as f1:
        num = 1
        while True:
            line_li = []
            # リストを用意し1レコード分のデータを取得
            for i in range(9):
                line_li.append(f1.readline())
            # データがなくなるとここでループを抜ける
            if not line_li[0]:
                break

            # 改行文字を取り除く
            line_li = [x.strip("\n") for x in line_li]

            # データを分割
            line_li[6:7] = line_li[6].split()

            title = line_li[0]
            topic_title = line_li[4]
            cate_index = line_li[1]
            area_index = line_li[2]
            photo = line_li[6]
            rec_date = line_li[7]
            exp = line_li[9]

            outstr = ""
            outstr += open(File_Format, encoding="utf-8").read()

            outstr = re.sub("%title%", title, outstr)
            outstr = re.sub("%topic_title%", topic_title, outstr)
            outstr = re.sub("%cate_index%", cate_index, outstr)
            outstr = re.sub("%area_index%", area_index, outstr)
            outstr = re.sub("%rec_date%", rec_date, outstr)
            outstr = re.sub("%photo%", photo, outstr)
            outstr = re.sub("%exp%", exp, outstr)

            html = infile.strip(".txt") + "_" + "{0:03d}".format(num) + ".html"

            with open("pages/" + html, "w", encoding="utf-8") as f2:
                f2.write(outstr)

            print("\t" + infile + "->" + html)
            print("\t" + "変換完了")
            num += 1
            print("<body><a href='https://www.mmdb.net/mlab/test/pages/" + html + "'>" + title + "<a></body>")

print("処理完了")
