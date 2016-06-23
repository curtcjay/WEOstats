from spyre import server
import pandas as pd
import indicators_preprocessing as ip
import indicators_stats_analysis as isa
import matplotlib
matplotlib.style.use('ggplot')


class EconoApp(server.App):
    title = "EconoApp"

    inputs = [{     "input_type":'dropdown',
                    "label": 'Country', 
                    "options" : [ {"label": "United States", "value":'United States'},
                                  {"label": "China", "value":'China'},
                                  {"label": "Japan", "value":'Japan'}],
                    "variable_name": 'country', 
                    "action_id": "update_data" },
              {     "input_type":'dropdown',
                    "label": 'Starting Year', 
                    "options" : [ {"label": "1980", "value":1980},
                                  {"label": "1981", "value":1981},
                                  {"label": "1982", "value":1982},
                                  {"label": "1983", "value":1983}],
                    "variable_name": 'year1', 
                    "action_id": "update_data" },
              {     "input_type":'dropdown',
                    "label": 'End Year', 
                    "options" : [ {"label": "1980", "value":1980},
                                  {"label": "1981", "value":1981},
                                  {"label": "1982", "value":1982},
                                  {"label": "1983", "value":1983}],
                    "variable_name": 'year2', 
                    "action_id": "update_data" },
              {     "input_type":'dropdown',
                    "label": 'Indicator', 
                    "options" : [ {"label": "Current Account Balance", "value":'BCA'},
                                  {"label": "General Government Revenue", "value":'GGR'},
                                  {"label": "General Government Structural Balance", "value":'GGSB'},
                                  {"label": "General Government Total Expenditure", "value":'GGX'},
                                  {"label": "General Government Gross Debt", "value":'GGXWDG'},
                                  {"label": "General Government Net Debt", "value":'GGXWDN'},
                                  {"label": "Employment", "value":'LE'},
                                  {"label": "Population", "value":'LP'},
                                  {"label": "Unemployment Rate", "value":'LUR'},
                                  {"label": "Output Gap as Percentage of GDP", "value":'NGAP_NPGDP'},
                                  {"label": "GDP constant", "value":'NGDP_R'},
                                  {"label": "GDP as percentage of GDP constant", "value":'NGDPRPC'},
                                  {"label": "Gross National Savings", "value":'NGSD_NGDP'},
                                  {"label": "Total Investment", "value":'NID_NGDP'},
                                  {"label": "Inflation end of period Consumer Prices", "value":'PCPIE'},
                                  {"label": "Volume of Exports of Goods and Services", "value":'TX_RPCH'}],
                    "variable_name": 'indicator', 
                    "action_id": "update_data" }]  # action_ids can point to controls
    
    # changing the input state now activates this control so we no longer need a button
    controls = [{   "control_type" : "button",  
                    "label" : "Update",
                    "control_id" : "update_data"}]

    tabs = ["Plot", "Table"]  # add tabs

    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",# must specify which tab each output should live in
                    "on_page_load" : True },
                {   "output_type" : "table",
                    "output_id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]


    def getData(self, params):
        country = params['country']
        year1   = params['year1']
        year2   = params['year2']
        indc    = params['indicator']
        
        df   = ip.indicators_preprocessing_by_year(indc)
        #gr   = isa.growth_rate(df,year1,year2,indc,country)
        #avg  = isa.average(df,year1,year2,indc,country)
        #stdr = isa.std(df,year1,year2,indc,country)
        df = pd.DataFrame(df)
        return df

    def getPlot(self, params):
        country = params['country']
        year1   = params['year1']
        year2   = params['year2']
        indc    = params['indicator']
        
        df  = ip.indicators_preprocessing_by_year(indc)
        
        fig = isa.time_series_plot(df, year1, year2, country, indc)
        return fig

app = EconoApp()
app.launch(port=9093)