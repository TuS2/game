con = sqlite3.connect('top_gamers.bd')
cur = con.cursor()
res = cur.update('''SELECT combinations FROM combs
                WHERE id = ?''', (int(iid),)).fetchall()
for i in res:
    self.out3.setText(str(i).strip("'(),'"))
# поиск описания в бд и вывод
con.commit()
con.close()
