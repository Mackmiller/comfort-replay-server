from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from django.http import JsonResponse
# from django.shortcuts import render
import pandas as pd

class RegisterData(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        result_data = []
        for file in request.FILES.values():
            # prints file name (should be ViewingActivity.csv)
            print(file)
            df = pd.read_csv(file)

            # check what you have imported. Should return number of rows of data
            print(df.shape)

            # drop columns that aren't needed for analysis
            df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)
            
            # preparing for time zone change by converting to .to_datetime
            df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
            
            # change the Start Time column into the dataframe's index (necessary for time conversion)
            df = df.set_index('Start Time')
            
            # convert from UTC timezone to eastern time using .tz_convert
            df.index = df.index.tz_convert('US/Eastern')
            
            # reset the index so that Start Time becomes a column again
            df = df.reset_index()
            
            # convert Duration column using .to_timedelta to prepare for filter
            df['Duration'] = pd.to_timedelta(df['Duration'])

            # filter data so that Duration (time watched) was at least 5 minutes. This filters out trailers and other short/extraneous viewings
            df = df[(df['Duration'] > '0 days 00:05:00')]

            # filter data so that Start Time (date watched) is no earlier than March 11, 2020
            # safe this to df_pandemic
            df_pandemic = df[(df['Start Time'] > '2020-3-10 23:59:59')]

            # create new column based on split occuring at the colon within the Title column
            # the colon is present any time there is an episode of a tv show, which is the data we are most interested in
            # by creating a new column at the split, we can work with just the title of the tv show, instead of the individual episodes for now
            df_pandemic['title_new'] = df_pandemic['Title'].str.split(':').str[0]

            # view first data row to see if all above code works
            print(df_pandemic.head(1))

            # assign Start Time content to new columns weekday and hour
            df_pandemic['weekday'] = df_pandemic['Start Time'].dt.weekday
            df_pandemic['hour'] = df_pandemic['Start Time'].dt.hour

            df_pandemic['hour'] = pd.Categorical(df_pandemic['hour'], categories=
            [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
            ordered=True)

            #count the rows that have each hour as their value
            df_by_hour = df_pandemic['hour'].value_counts()

            # sort index using our categorical, 0-23
            df_by_hour = df_by_hour.sort_index()
            # convert daily data to json
            data3 = df_by_hour.to_json(orient="index")


            # get top ten shows
            top_ten = df_pandemic['title_new'].value_counts().head(10)
            # convert show data to json
            data2 = top_ten.to_json(orient="index")

            # get top show
            top_show = df_pandemic['title_new'].value_counts().head(1)
            data4 = top_show.to_json(orient="index")

            #convert whole file to json
            # data = df_pandemic.to_json(orient = 'records', date_format='iso', date_unit='s')

            # return JsonResponse(data, safe=False)
            return JsonResponse((data2,data3, data4), safe=False)
      


        # return JsonResponse(data, safe=False)
        return Response({"success": "Good job, buddy"})
        # return render(request, 'index.html', context=mydict)