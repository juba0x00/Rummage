
# def BreachChecker(self):
#     self.SearchKey = urllib.parse.quote(self.SearchKey)
#     print(self.SearchKey)
#     res = get(f"http://breachchecker.com/set-account/{self.SearchKey}/", allow_redirects=True)
#     soup = BeautifulSoup(res.content, "lxml")
#     _, self.__BreachedRecord, self.__LastBreach = soup.find_all("div", {"class": "font-big"})
#     self.__BreachedRecord, self.__LastBreach = self.__BreachedRecord.text, self.__LastBreach.text
#     self.__RiskLevel = str(str(soup.find_all("div", {"class": "progress"})).split("width:")[1])[:3]
#     print(f"breach rec = {self.__BreachedRecord} \n last breach = {self.__LastBreach} \n risk = {self.__RiskLevel}")
