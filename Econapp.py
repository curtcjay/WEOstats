from spyre import server
import pandas as pd
import indicators_preprocessing as ip
import indicators_stats_analysis as isa
import matplotlib
matplotlib.style.use('fivethirtyeight')


class EconoApp(server.App):
    title = "MacroSTAT"

    inputs = [{"input_type": 'dropdown',
               "label": 'Country',
               "options": [{"label": "Afghanistan", "value": 'Afghanistan'},
                           {"label": "Albania", "value": 'Albania'},
                           {"label": "Algeria", "value": 'Algeria'},
                           {"label": "Angola", "value": 'Angola'},
                           {"label": "Antigua and Barbuda", "value": 'Antigua and Barbuda'},
                           {"label": "Argentina", "value": 'Argentina'},
                           {"label": "Armenia", "value": 'Armenia'},
                           {"label": "Australia", "value": 'Australia'},
                           {"label": "Azerbaijian", "value": 'Azerbaijian'},
                           {"label": "Bahrain", "value": 'Bahrain'},
                           {"label": "Bangladesh", "value": 'Bangladesh'},
                           {"label": "Barbados", "value": 'Barbados'},
                           {"label": "Belarus", "value": 'Belarus'},
                           {"label": "Belgium", "value": 'Belgium'},
                           {"label": "Belize", "value": 'Belize'},
                           {"label": "Benin", "value": 'Benin'},
                           {"label": "Bhutan", "value": 'Bhutan'},
                           {"label": "Bolivia", "value": 'Bolivia'},
                           {"label": "Bosnia and Herzegovina", "value": 'Bosnia and Herzegovina'},
                           {"label": "Botswana", "value": 'Botswana'},
                           {"label": "Brazil", "value": 'Brazil'},
                           {"label": "Brunei Darussalam", "value": 'Brunei Darussalam'},
                           {"label": "Bulgaria", "value": 'Bulgaria'},
                           {"label": "Burkina Faso", "value": 'Burkina Faso'},
                           {"label": "Burundi", "value": 'Burundi'},
                           {"label": "Cabo Verde", "value": 'Cabo Verde'},
                           {"label": "Cambodia", "value": 'Cambodia'},
                           {"label": "Cameroon", "value": 'Cameroon'},
                           {"label": "Canada", "value": 'Canada'},
                           {"label": "Central African Republic", "value": 'Central African Republic'},
                           {"label": "Chad", "value": 'Chad'},
                           {"label": "Chile", "value": 'Chile'},
                           {"label": "China", "value": 'China'},
                           {"label": "Colombia", "value": 'Colombia'},
                           {"label": "Comoros", "value": 'Comoros'},
                           {"label": "Costa Rica", "value": 'Costa Rica'},
                           {"label": "Cote d'Ivoire", "value": "Cote d'Ivoire"},
                           {"label": "Croatia", "value": 'Croatia'},
                           {"label": "Cyprus", "value": 'Cyprus'},
                           {"label": "Czech Republic", "value": 'Czech Republic'},
                           {"label": "Democratic Republic of the Congo", "value": 'Democratic Republic of the Congo'},
                           {"label": "Denmark", "value": 'Denmark'},
                           {"label": "Djibouti", "value": 'Djibouti'},
                           {"label": "Dominica", "value": 'Dominica'},
                           {"label": "Dominican Republic", "value": 'Dominican Republic'},
                           {"label": "Ecuador", "value": 'Ecuador'},
                           {"label": "Egypt", "value": 'Egypt'},
                           {"label": "El Salvador", "value": 'El Salvador'},
                           {"label": "Equatorial Guinea", "value": 'Equatorial Guinea'},
                           {"label": "Eritrea", "value": 'Eritrea'},
                           {"label": "Estonia", "value": 'Estonia'},
                           {"label": "Ethiopia", "value": 'Ethiopia'},
                           {"label": "Fiji", "value": 'Fiji'},
                           {"label": "Finland", "value": 'Finland'},
                           {"label": "France", "value": 'France'},
                           {"label": "FYR Macedonia", "value": 'FYR Macedonia'},
                           {"label": "Gabon", "value": 'Gabon'},
                           {"label": "Georgia", "value": 'Georgia'},
                           {"label": "Germany", "value": 'Germany'},
                           {"label": "Ghana", "value": 'Ghana'},
                           {"label": "Greece", "value": 'Greece'},
                           {"label": "Grenada", "value": 'Grenada'},
                           {"label": "Guatemala", "value": 'Guatemala'},
                           {"label": "Guinea", "value": 'Guinea'},
                           {"label": "Guinea-Bissau", "value": 'Guinea-Bissau'},
                           {"label": "Guyana", "value": 'Guyana'},
                           {"label": "Haiti", "value": 'Haiti'},
                           {"label": "Honduras", "value": 'Honduras'},
                           {"label": "Hong Kong SAR", "value": 'Hong Kong SAR'},
                           {"label": "Hungary", "value": 'Hungary'},
                           {"label": "Iceland", "value": 'Iceland'},
                           {"label": "India", "value": 'India'},
                           {"label": "Indonesia", "value": 'Indonesia'},
                           {"label": "Iraq", "value": 'Iraq'},
                           {"label": "Ireland", "value": 'Ireland'},
                           {"label": "Islamic Republic of Iran", "value": 'Islamic Republic of Iran'},
                           {"label": "Israel", "value": 'Israel'},
                           {"label": "Italy", "value": 'Italy'},
                           {"label": "Jamaica", "value": 'Jamaica'},
                           {"label": "Japan", "value": 'Japan'},
                           {"label": "Jordan", "value": 'Jordan'},
                           {"label": "Kazakhstan", "value": 'Kazakhstan'},
                           {"label": "Kenya", "value": 'Kenya'},
                           {"label": "Kiribati", "value": 'Kiribati'},
                           {"label": "Korea", "value": 'Korea'},
                           {"label": "Kosovo", "value": 'Kosovo'},
                           {"label": "Kuwait", "value": 'Kuwait'},
                           {"label": "Kyrgyz Republic", "value": 'Kyrgyz Republic'},
                           {"label": "Lao P.D.R.", "value": 'Lao P.D.R.'},
                           {"label": "Latvia", "value": 'Latvia'},
                           {"label": "Lebanon", "value": 'Lebanon'},
                           {"label": "Lesotho", "value": 'Lesotho'},
                           {"label": "Liberia", "value": 'Liberia'},
                           {"label": "Libya", "value": 'Libya'},
                           {"label": "Lithuania", "value": 'Lithuania'},
                           {"label": "Luxembourg", "value": 'Luxembourg'},
                           {"label": "Macao SAR", "value": 'Macao SAR'},
                           {"label": "Madagascar", "value": 'Madagascar'},
                           {"label": "Malawi", "value": 'Malawi'},
                           {"label": "Malaysia", "value": 'Malaysia'},
                           {"label": "Maldives", "value": 'Maldives'},
                           {"label": "Mali", "value": 'Mali'},
                           {"label": "Malta", "value": 'Malta'},
                           {"label": "Marshall Islands", "value": 'Marshall Islands'},
                           {"label": "Mauritania", "value": 'Mauritania'},
                           {"label": "Mauritius", "value": 'Mauritius'},
                           {"label": "Mexico", "value": 'Mexico'},
                           {"label": "Micronesia", "value": 'Micronesia'},
                           {"label": "Moldova", "value": 'Moldova'},
                           {"label": "Mongolia", "value": 'Mongolia'},
                           {"label": "Montenegro", "value": 'Montenegro'},
                           {"label": "Morocco", "value": 'Morocco'},
                           {"label": "Mozambique", "value": 'Mozambique'},
                           {"label": "Myanmar", "value": 'Myanmar'},
                           {"label": "Namibia", "value": 'Namibia'},
                           {"label": "Nepal", "value": 'Nepal'},
                           {"label": "Netherlands", "value": 'Netherlands'},
                           {"label": "New Zealand", "value": 'New Zealand'},
                           {"label": "Nicaragua", "value": 'Nicaragua'},
                           {"label": "Niger", "value": 'Niger'},
                           {"label": "Nigeria", "value": 'Nigeria'},
                           {"label": "Norway", "value": 'Norway'},
                           {"label": "Oman", "value": 'Oman'},
                           {"label": "Pakistan", "value": 'Pakistan'},
                           {"label": "Palau", "value": 'Palau'},
                           {"label": "Panama", "value": 'Panama'},
                           {"label": "Papua New Guinea", "value": 'Papua New Guinea'},
                           {"label": "Paraguay", "value": 'Paraguay'},
                           {"label": "Peru", "value": 'Peru'},
                           {"label": "Philippines", "value": 'Philippines'},
                           {"label": "Poland", "value": 'Poland'},
                           {"label": "Portugal", "value": 'Portugal'},
                           {"label": "Puerto Rico", "value": 'Puerto Rico'},
                           {"label": "Qatar", "value": 'Qatar'},
                           {"label": "Republic of Congo", "value": 'Republic of Congo'},
                           {"label": "Romania", "value": 'Romania'},
                           {"label": "Russia", "value": 'Russia'},
                           {"label": "Rwanda", "value": 'Rwanda'},
                           {"label": "Samoa", "value": 'Samoa'},
                           {"label": "San Marino", "value": 'San Marino'},
                           {"label": "Sao Tome and Principe", "value": 'Sao Tome and Principe'},
                           {"label": "Saudi Arabia", "value": 'Saudi Arabia'},
                           {"label": "Senegal", "value": 'Senegal'},
                           {"label": "Serbia", "value": 'Serbia'},
                           {"label": "Seychelles", "value": 'Seychelles'},
                           {"label": "Sierra Leone", "value": 'Sierra Leone'},
                           {"label": "Singapore", "value": 'Singapore'},
                           {"label": "Slovak Republic", "value": 'Slovak Republic'},
                           {"label": "Slovenia", "value": 'Slovenia'},
                           {"label": "Solomon Islands", "value": 'Solomon Islands'},
                           {"label": "South Africa", "value": 'South Africa'},
                           {"label": "South Sudan", "value": 'South Sudan'},
                           {"label": "Spain", "value": 'Spain'},
                           {"label": "Sri Lanka", "value": 'Sri Lanka'},
                           {"label": "St. Kitts and Nevis", "value": 'St. Kitts and Nevis'},
                           {"label": "St. Lucia", "value": 'St. Lucia'},
                           {"label": "St. Vincent and the Grenadines", "value": 'St. Vincent and the Grenadines'},
                           {"label": "Sudan", "value": 'Sudan'},
                           {"label": "Suriname", "value": 'Suriname'},
                           {"label": "Swaziland", "value": 'Swaziland'},
                           {"label": "Sweden", "value": 'Sweden'},
                           {"label": "Switzerland", "value": 'Switzerland'},
                           {"label": "Syria", "value": 'Syria'},
                           {"label": "Taiwan Province of China", "value": 'Taiwan Province of China'},
                           {"label": "Tajikistan", "value": 'Tajikistan'},
                           {"label": "Tanzania", "value": 'Tanzania'},
                           {"label": "Thailand", "value": 'Thailand'},
                           {"label": "The Bahamas", "value": 'The Bahamas'},
                           {"label": "The Gambia", "value": 'The Gambia'},
                           {"label": "Timor-Leste", "value": 'Timor-Leste'},
                           {"label": "Togo", "value": 'Togo'},
                           {"label": "Tonga", "value": 'Tonga'},
                           {"label": "Trinidad and Tobago", "value": 'Trinidad and Tobago'},
                           {"label": "Tunisia", "value": 'Tunisia'},
                           {"label": "Turkey", "value": 'Turkey'},
                           {"label": "Turkmenistan", "value": 'Turkmenistan'},
                           {"label": "Tuvalu", "value": 'Tuvalu'},
                           {"label": "Uganda", "value": 'Uganda'},
                           {"label": "Ukraine", "value": 'Ukraine'},
                           {"label": "United Arab Emirates", "value": 'United Arab Emirates'},
                           {"label": "United Kingdom", "value": 'United Kingdom'},
                           {"label": "United States", "value": 'United States'},
                           {"label": "Uruguay", "value": 'Uruguay'},
                           {"label": "Uzbekistan", "value": 'Uzbekistan'},
                           {"label": "Vanuatu", "value": 'Vanuatu'},
                           {"label": "Venezuela", "value": 'Venezuela'},
                           {"label": "Vietnam", "value": 'Vietnam'},
                           {"label": "Yemen", "value": 'Yemen'},
                           {"label": "Zambia", "value": 'Zambia'},
                           {"label": "Zimbabwe", "value": 'Zimbabwe'}],
               "variable_name": 'country',
               "action_id": "button"},
              {"input_type": 'dropdown',
               "label": 'Starting Year',
               "options": [{"label": "1980", "value": 1980},
                           {"label": "1981", "value": 1981},
                           {"label": "1982", "value": 1982},
                           {"label": "1983", "value": 1983},
                           {"label": "1984", "value": 1984},
                           {"label": "1985", "value": 1985},
                           {"label": "1986", "value": 1986},
                           {"label": "1987", "value": 1987},
                           {"label": "1988", "value": 1988},
                           {"label": "1989", "value": 1989},
                           {"label": "1990", "value": 1990},
                           {"label": "1991", "value": 1991},
                           {"label": "1992", "value": 1992},
                           {"label": "1993", "value": 1993},
                           {"label": "1994", "value": 1994},
                           {"label": "1995", "value": 1995},
                           {"label": "1996", "value": 1996},
                           {"label": "1997", "value": 1997},
                           {"label": "1998", "value": 1998},
                           {"label": "1999", "value": 1999},
                           {"label": "2000", "value": 2000},
                           {"label": "2001", "value": 2001},
                           {"label": "2002", "value": 2002},
                           {"label": "2003", "value": 2003},
                           {"label": "2004", "value": 2004},
                           {"label": "2005", "value": 2005},
                           {"label": "2006", "value": 2006},
                           {"label": "2007", "value": 2007},
                           {"label": "2008", "value": 2008},
                           {"label": "2009", "value": 2009},
                           {"label": "2010", "value": 2010},
                           {"label": "2011", "value": 2011},
                           {"label": "2012", "value": 2012},
                           {"label": "2013", "value": 2013},
                           {"label": "2014", "value": 2014},
                           {"label": "2015", "value": 2015}],
               "variable_name": 'year1',
               "action_id": "button"},
              {"input_type": 'dropdown',
               "label": 'End Year',
               "options": [{"label": "1980", "value": 1980},
                           {"label": "1981", "value": 1981},
                           {"label": "1982", "value": 1982},
                           {"label": "1983", "value": 1983},
                           {"label": "1984", "value": 1984},
                           {"label": "1985", "value": 1985},
                           {"label": "1986", "value": 1986},
                           {"label": "1987", "value": 1987},
                           {"label": "1988", "value": 1988},
                           {"label": "1989", "value": 1989},
                           {"label": "1990", "value": 1990},
                           {"label": "1991", "value": 1991},
                           {"label": "1992", "value": 1992},
                           {"label": "1993", "value": 1993},
                           {"label": "1994", "value": 1994},
                           {"label": "1995", "value": 1995},
                           {"label": "1996", "value": 1996},
                           {"label": "1997", "value": 1997},
                           {"label": "1998", "value": 1998},
                           {"label": "1999", "value": 1999},
                           {"label": "2000", "value": 2000},
                           {"label": "2001", "value": 2001},
                           {"label": "2002", "value": 2002},
                           {"label": "2003", "value": 2003},
                           {"label": "2004", "value": 2004},
                           {"label": "2005", "value": 2005},
                           {"label": "2006", "value": 2006},
                           {"label": "2007", "value": 2007},
                           {"label": "2008", "value": 2008},
                           {"label": "2009", "value": 2009},
                           {"label": "2010", "value": 2010},
                           {"label": "2011", "value": 2011},
                           {"label": "2012", "value": 2012},
                           {"label": "2013", "value": 2013},
                           {"label": "2014", "value": 2014},
                           {"label": "2015", "value": 2015}],
               "variable_name": 'year2',
               "action_id": "button"},
              {"input_type": 'dropdown',
               "label": 'Indicator',
               "options": [{"label": "Current Account Balance", "value": 'BCA'},
                           {"label": "General Government Revenue", "value": 'GGR'},
                           {"label": "General Government Structural Balance", "value": 'GGSB'},
                           {"label": "General Government Total Expenditure", "value": 'GGX'},
                           {"label": "General Government Gross Debt", "value": 'GGXWDG'},
                           {"label": "General Government Net Debt", "value": 'GGXWDN'},
                           {"label": "Employment", "value": 'LE'},
                           {"label": "Population", "value": 'LP'},
                           {"label": "Unemployment Rate", "value": 'LUR'},
                           {"label": "Output Gap as Percentage of GDP", "value": 'NGAP_NPGDP'},
                           {"label": "GDP constant", "value": 'NGDP_R'},
                           {"label": "GDP as percentage of GDP constant", "value": 'NGDPRPC'},
                           {"label": "Gross National Savings", "value": 'NGSD_NGDP'},
                           {"label": "Total Investment", "value": 'NID_NGDP'},
                           {"label": "Inflation end of period Consumer Prices", "value": 'PCPIE'},
                           {"label": "Volume of Exports of Goods and Services", "value": 'TX_RPCH'}],
               "variable_name": 'indicator',
               "action_id": "button"}]  # action_ids can point to controls

    # changing the input state now activates this control so we no longer need a button
    controls = [{"control_type": "button",
                 "label": "Update",
                 "control_id": "update_data"},
                {"control_type": "button",
                 "label": "Download",
                 "control_id": "update_data"}]

    tabs = ["Plot", "Foot"]  # add tabs

    outputs = [{"output_type": "plot",
                "output_id": "plot",
                "control_id": "update_data",
                "tab": "Plot",  # must specify which tab each output should live in
                "on_page_load": True},
               {"output_type": "table",
                "output_id": "table_id",
                "control_id": "update_data",
                "tab": "Foot",
                "on_page_load": True}]

    def getData(self, params):
        country = params['country']
        year1 = params['year1']
        year2 = params['year2']
        indc = params['indicator']

        df = ip.indicators_preprocessing_for_table(indc)
        df = pd.DataFrame(df)
        return df

    def getPlot(self, params):
        country = params['country']
        year1 = params['year1']
        year2 = params['year2']
        indc = params['indicator']

        indicator_dict = {'BCA': "Current Account Balance",
                          'GGR': "General Government Revenue",
                          'GGSB': "General Government Structural Balance",
                          'GGX': "General Government Total Expenditure",
                          'GGXWDG': "General Government Gross Debt",
                          'GGXWDN': "General Government Net Debt",
                          'LE': "Employment",
                          'LP': "Population",
                          'LUR': "Unemployment Rate",
                          'NGAP_NPGDP': "Output Gap as Percentage of GDP",
                          'NGDP_R': "GDP constant",
                          'NGDPRPC': "GDP as percentage of GDP constant",
                          'NGSD_NGDP': "Gross National Savings",
                          'NID_NGDP': "Total Investment",
                          'PCPIE': "Inflation end of period Consumer Prices",
                          'TX_RPCH': "Volume of Exports of Goods and Services"}

        scale_dict = {'BCA': "U.S. dollars - Billions",
                      'GGR': "National currency - Billions",
                      'GGSB': "National currency - Billions",
                      'GGX': "National currency - Billions",
                      'GGXWDG': "National currency - Billions",
                      'GGXWDN': "National currency - Billions",
                      'LE': "Persons - Millions",
                      'LP': "Persons - Millions",
                      'LUR': "Percent of total labor force",
                      'NGAP_NPGDP': "Percent of potential GDP",
                      'NGDP_R': "National currency - Billions",
                      'NGDPRPC': "National currency - Units",
                      'NGSD_NGDP': "Percent of GDP",
                      'NID_NGDP': "Percent of GDP",
                      'PCPIE': "Index",
                      'TX_RPCH': "Percent change"}

        df = ip.indicators_preprocessing_by_year(indc)
        fig = isa.time_series_plot(df, year1, year2, country, indc)
        fig.set_title(indicator_dict[params['indicator']])
        fig.set_ylabel(scale_dict[params['indicator']])
        return fig


app = EconoApp()
app.launch(port=9990)
