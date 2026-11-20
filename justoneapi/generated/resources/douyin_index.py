from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinIndexResource(BaseResource):
    """Generated resource for Douyin Index."""

    def get_keyword_trends_v1(
        self,
        *,
        since: str,
        until: str,
        keyword: str | None = None,
        keywords: list[Any] | None = None,
    ) -> ApiResponse[Any]:
        """
        Keyword Trends

        Retrieves Douyin Index (Ocean Engine trend index) keyword trends for one keyword or up to five keywords over an inclusive date range in China time (UTC+8). Use it for topic research and comparing keyword interest over time.

        Args:
            since: First day to include. Use YYYY-MM-DD or an RFC 3339 timestamp with a timezone; timestamps are interpreted as calendar days in China time (UTC+8).
            until: Last day to include, in the same format as since, on or after since in China time (UTC+8). Figures are usually published one or two days later.
            keyword: One keyword, at most 50 characters without commas. Provide exactly one of keyword or keywords; letter case does not matter.
            keywords: One to five keywords, separated by commas or supplied as repeated query parameters. Each keyword must contain at most 50 characters without commas. Provide exactly one of keyword or keywords; letter case does not matter.
        """
        return self._get(
            "/api/douyin-index/get-keyword-trends/v1",
            {
                "since": since,
                "until": until,
                "keyword": keyword,
                "keywords": keywords,
            },
        )

    def get_realtime_hotspots_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Realtime Hotspots

        Retrieves the current hotspot lists from Douyin Index in Creator Center. Use it to monitor trending topics and plan timely content.
        """
        return self._get(
            "/api/douyin-index/get-realtime-hotspots/v1",
            {},
        )

    def get_creation_guide_v1(
        self,
        *,
        analysis_type: str,
        data_type: str,
        vertical: str | None = None,
        period: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Creation Guide

        Retrieves a selected ranking, production report, consumption report, or publication calendar from the Douyin Creator Center Creation Guide. Use content verticals and published reporting dates to research popular keywords, topics, videos, and audience trends.

        Args:
            analysis_type: Creation Guide analysis tab.  Available Values: - `CREATIVITY`: Creative insights and rankings - `PRODUCTION`: Content production analysis - `CONSUMPTION`: Content consumption analysis
            data_type: One data set within the selected tab. Choose KEYWORDS, TOPICS, or VIDEOS for creative insight rankings.  Available Values: - `CONTENT_DATES`: Publication calendar for keyword and topic rankings and for production and consumption reports - `VIDEO_DATES`: Publication calendar for popular video rankings. Use with CREATIVITY - `KEYWORDS`: Popular keywords. Use with CREATIVITY - `TOPICS`: Popular topics. Use with CREATIVITY - `VIDEOS`: Popular videos. Use with CREATIVITY - `PUBLISH_TREND`: Content publishing trend. Use with PRODUCTION - `AUTHOR_PORTRAIT`: Creator profile distribution. Use with PRODUCTION - `VIDEO_DURATION`: Content share, engagement, and completion by video duration. Use with PRODUCTION or CONSUMPTION - `CONSUME_TREND`: Content supply and consumption trends. Use with CONSUMPTION - `INTERACT_TREND`: Content engagement trend. Use with CONSUMPTION - `CONSUMER_PORTRAIT`: Audience distributions for viewing and engagement. Use with CONSUMPTION
            vertical: Content vertical. Required for rankings and reports. Omit for publication calendars.  Available Values: - `DRAMA`: Scripted stories and drama - `CELEBRITIES`: Celebrities - `MUSIC`: Music - `ANIME_COMICS`: Anime, comics, and related fan culture - `GAMING`: Gaming - `CURRENT_AFFAIRS`: Society and current affairs - `DANCE`: Dance - `RURAL_LIFE`: Agriculture, rural areas, and rural life - `TECHNOLOGY`: Science and technology - `FINANCE`: Business and finance - `PARENTING`: Maternity and parenting - `LIFESTYLE_HOME`: Lifestyle and home - `HEALTH`: Medicine and health - `RELATIONSHIPS`: Relationships and emotional well-being - `CULTURE`: Culture - `CAREERS`: Careers and the workplace - `EDUCATION`: Education and campus life - `PHOTOGRAPHY`: Photography and videography - `FOOD`: Food and cooking - `TRAVEL`: Travel - `FASHION`: Fashion - `SPORTS`: Sports - `ENTERTAINMENT`: Leisure and entertainment - `AUTOMOTIVE`: Cars and the automotive industry
            period: ONE_DAY, THREE_DAYS, or WEEK for rankings. WEEK or MONTH for profile and video duration reports. Omit for trend reports and publication calendars.  Available Values: - `ONE_DAY`: One published day. Rankings only - `THREE_DAYS`: Three days ending on the specified published day. Rankings only - `WEEK`: A reporting week ending on Sunday - `MONTH`: A calendar month. Profile and video duration reports only
            start_date: Inclusive first day in China time (UTC+8), in YYYY-MM-DD format. Required for publishing, supply and consumption, and engagement trends. Omit for other data types.
            end_date: Inclusive last day in China time (UTC+8), in YYYY-MM-DD format. Required for rankings and reports. Use a published Sunday for WEEK or a published month end for MONTH. Omit for publication calendars.
        """
        return self._get(
            "/api/douyin-index/get-creation-guide/v1",
            {
                "analysisType": analysis_type,
                "dataType": data_type,
                "vertical": vertical,
                "period": period,
                "startDate": start_date,
                "endDate": end_date,
            },
        )
