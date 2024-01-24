import time, math


cal_ID = 0

class MonthlyCalendar:
    def __init__(self, year = None, month = None):
        self.tFontFace = 'Arial, Helvetica'
        self.tFontSize = 12                
        self.tFontColor = '#FFFFFF'         
        self.tBGColor = '#304B90'          

        self.hFontFace = 'Arial, Helvetica' 
        self.hFontSize = 10                 
        self.hFontColor = '#FFFFFF'        
        self.hBGColor = '#304B90'          

        self.dFontFace = 'Arial, Helvetica'
        self.dFontSize = 12                 
        self.dFontColor = '#000000'         
        self.dBGColor = '#FFFFFF'           

        self.wFontFace = 'Arial, Helvetica' 
        self.wFontSize = 10                 
        self.wFontColor = '#FFFFFF'         
        self.wBGColor = '#304B90'           

        self.saFontColor = '#0000D0'       
        self.saBGColor = '#F6F6FF'          

        self.suFontColor = '#D00000'        
        self.suBGColor = '#FFF0F0'          

        self.tdBorderColor = 'red'      

        self.borderColor = '#304B90'        
        self.hilightColor = '#FFFF00'       

        self.link = ''                      
        self.offset = 1                    
        self.weekNumbers = 0                

        self.weekdays = ('Sob', 'Nd', 'Pn', 'Wt', 'Sr', 'Czw', 'Pt')

        self.months = ('Styczen', 'Luty', 'Marzec', 'Kwiecien', 'Maj', 'Czerwiec',
                       'Lipiec', 'Sierpien', 'Wrzesien', 'Pazdziernik', 'Listopad', 'Grudzien')

        self.error = ('Year must be 1 - 3999!', 'Month must be 1 - 12!')

        if year is None and month is None:
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
        elif year is None and month is not None: year = time.localtime().tm_year
        elif month is None: month = 1
        self.year = int(year)
        self.month = int(month)
        self.specDays = {}

    __size = 0
    __mDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def set_styles(self):
        globals()['cal_ID'] += 1
        html = '<style> .cssTitle' + str(globals()['cal_ID']) + ' { '
        if self.tFontFace: html += 'font-family: ' + self.tFontFace + '; '
        if self.tFontSize: html += 'font-size: ' + str(self.tFontSize) + 'px; '
        if self.tFontColor: html += 'color: ' + self.tFontColor + '; '
        if self.tBGColor: html += 'background-color: ' + self.tBGColor + '; '
        html += '} .cssHeading' + str(globals()['cal_ID']) + ' { '
        if self.hFontFace: html += 'font-family: ' + self.hFontFace + '; '
        if self.hFontSize: html += 'font-size: ' + str(self.hFontSize) + 'px; '
        if self.hFontColor: html += 'color: ' + self.hFontColor + '; '
        if self.hBGColor: html += 'background-color: ' + self.hBGColor + '; '
        html += '} .cssDays' + str(globals()['cal_ID']) + ' { '
        if self.dFontFace: html += 'font-family: ' + self.dFontFace + '; '
        if self.dFontSize: html += 'font-size: ' + str(self.dFontSize) + 'px; '
        if self.dFontColor: html += 'color: ' + self.dFontColor + '; '
        if self.dBGColor: html += 'background-color: ' + self.dBGColor + '; '
        html += '} .cssWeeks' + str(globals()['cal_ID']) + ' { '
        if self.wFontFace: html += 'font-family: ' + self.wFontFace + '; '
        if self.wFontSize: html += 'font-size: ' + str(self.wFontSize) + 'px; '
        if self.wFontColor: html += 'color: ' + self.wFontColor + '; '
        if self.wBGColor: html += 'background-color: ' + self.wBGColor + '; '
        html += '} .cssSaturdays' + str(globals()['cal_ID']) + ' { '
        if self.dFontFace: html += 'font-family: ' + self.dFontFace + '; '
        if self.dFontSize: html += 'font-size: ' + str(self.dFontSize) + 'px; '
        if self.saFontColor: html += 'color: ' + self.saFontColor + '; '
        if self.saBGColor: html += 'background-color: ' + self.saBGColor + '; '
        html += '} .cssSundays' + str(globals()['cal_ID']) + ' { '
        if self.dFontFace: html += 'font-family: ' + self.dFontFace + '; '
        if self.dFontSize: html += 'font-size: ' + str(self.dFontSize) + 'px; '
        if self.suFontColor: html += 'color: ' + self.suFontColor + '; '
        if self.suBGColor: html += 'background-color: ' + self.suBGColor + '; '
        html += '} .cssHilight' + str(globals()['cal_ID']) + ' { '
        if self.dFontFace: html += 'font-family: ' + self.dFontFace + '; '
        if self.dFontSize: html += 'font-size: ' + str(self.dFontSize) + 'px; '
        if self.dFontColor: html += 'color: ' + self.dFontColor + '; '
        if self.hilightColor: html += 'background-color: ' + self.hilightColor + '; '
        html += 'cursor: default; '
        html += '} </style>'
        return html

    def leap_year(self, year):
        return not (year % 4) and (year < 1582 or year % 100 or not (year % 400))

    def get_weekday(self, year, days):
        a = days
        if year: a += (year - 1) * 365
        for i in range(1, year):
            if self.leap_year(i): a += 1
        if year > 1582 or (year == 1582 and days >= 277): a -= 10
        if a: a = (a - self.offset) % 7
        elif self.offset: a += 7 - self.offset
        return a

    def get_week(self, year, days):
        firstWDay = self.get_weekday(year, 0)
        return int(math.floor((days + firstWDay) / 7) + (firstWDay <= 3))

    def table_cell(self, content, cls, date = '', style = ''):
        size = int(round(self.__size * 1.5))
        html = '<td align=center width=' + str(size) + ' class="' + cls + '"'

        if content != '&nbsp;' and cls.lower().find('day') != -1:
            link = self.link

            if len(self.specDays) > 0:
                if self.specDays[content][0]:
                    style += 'background-color:' + self.specDays[content][0] + ';'
                if self.specDays[content][1]:
                    html += ' title="' + self.specDays[content][1] + '"'
                if self.specDays[content][2]:
                    link = self.specDays[content][2]
                    style += 'cursor:pointer' + ';'
                else:
                    link='brak'
                    style += 'cursor:pointer' + ';'
                     
            if link=='brak':
                html += ' onMouseOver="this.className=\'cssHilight' + str(globals()['cal_ID']) + '\'"'
                html += ' onMouseOut="this.className=\'' + cls + '\'"'
                html += ' onClick="document.location.href=\'' + '?date=' + date + '\'"'
            
            
            if link and link!='brak':
                html += ' onMouseOver="this.className=\'cssHilight' + str(globals()['cal_ID']) + '\'"'
                html += ' onMouseOut="this.className=\'' + cls + '\'"'
                html += ' onClick="document.location.href=\'' + link + '?date=' + date + '\'"'
        if style: html += ' style="' + style + '"'
        html += '>' + content + '</td>'
        return html

    def table_head(self, content):
        cols = self.weekNumbers and '8' or '7'
        html = '<tr><td colspan=' + cols + ' class="cssTitle' + str(globals()['cal_ID']) + '" align=center><b>' + \
               content + '</b></td></tr><tr>'
        for i in range(len(self.weekdays)):
            ind = (i + self.offset) % 7
            wDay = self.weekdays[ind]
            html += self.table_cell(wDay, 'cssHeading' + str(globals()['cal_ID']))
        if self.weekNumbers: html += self.table_cell('&nbsp;', 'cssHeading' + str(globals()['cal_ID']))
        html += '</tr>'
        return html

    def viewEvent(self, start, end, color, title, link = ''):
        if start > end: return
        if start < 1 or start > 31: return
        if end < 1 or end > 31: return
        while start <= end:
            self.specDays[str(start)] = [color, title, link]
            start += 1

    def create(self):
        self.__size = (self.hFontSize > self.dFontSize) and self.hFontSize or self.dFontSize
        if self.wFontSize > self.__size: self.__size = self.wFontSize

        date = time.strftime('%Y-%m-%d', time.localtime())
        (curYear, curMonth, curDay) = [int(v) for v in date.split('-')]

        if self.year < 1 or self.year > 3999: html = '<b>' + self.error[0] + '</b>'
        elif self.month < 1 or self.month > 12: html = '<b>' + self.error[1] + '</b>'
        else:
            if self.leap_year(self.year): self.__mDays[1] = 29
            days = 0
            for i in range(self.month - 1): days += self.__mDays[i]

            start = self.get_weekday(self.year, days)
            stop = self.__mDays[self.month-1]

            html = self.set_styles()
            html += '<table border=1 cellspacing=0 cellpadding=0><tr>'
            html += '<td' + (self.borderColor and ' bgcolor=' + self.borderColor) + '>'
            html += '<table border=0 cellspacing=1 cellpadding=3>'
            title = self.months[self.month-1] + ' ' + str(self.year)
            html += self.table_head(title)
            daycount = 1

            if self.year == curYear and self.month == curMonth: inThisMonth = 1
            else: inThisMonth = 0

            if self.weekNumbers: weekNr = self.get_week(self.year, days)

            while daycount <= stop:
                html += '<tr>'
                wdays = 0

                for i in range(len(self.weekdays)):
                    ind = (i + self.offset) % 7
                    if ind == 0: cls = 'cssSaturdays'
                    elif ind == 1: cls = 'cssSundays'
                    else: cls = 'cssDays'

                    style = ''
                    date = "%s-%s-%s" % (self.year, self.month, daycount)

                    if (daycount == 1 and i < start) or daycount > stop: content = '&nbsp;'
                    else:
                        content = str(daycount)
                        if inThisMonth and daycount == curDay:
                            style = 'padding:0px;border:3px solid ' + self.tdBorderColor + ';'
                        elif self.year == 1582 and self.month == 10 and daycount == 4: daycount = 14
                        daycount += 1
                        wdays += 1

                    html += self.table_cell(content, cls + str(globals()['cal_ID']), date, style)

                if self.weekNumbers:
                    if not weekNr:
                        if self.year == 1: content = '&nbsp;'
                        elif self.year == 1583: content = '52'
                        else: content = str(self.get_week(self.year - 1, 365))
                    elif self.month == 12 and weekNr >= 52 and wdays < 4: content = '1'
                    else: content = str(weekNr)

                    html += self.table_cell(content, 'cssWeeks' + str(globals()['cal_ID']))
                    weekNr += 1

                html += '</tr>'
            html += '</table></td></tr></table>'
        return html


if __name__ == "__main__":
    filepath = "calendar.html"
    calendar = MonthlyCalendar()
    body = calendar.create()
    html = f"<!DOCTYPE html><html><body>{body}</body></html>"
    file = open(filepath, "w")
    file.write(html)
    file.close()
    