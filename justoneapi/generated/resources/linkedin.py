from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class LinkedinResource(BaseResource):
    """Generated resource for LinkedIn."""

    def search_user_v1(
        self,
        *,
        name: str | None = "",
        first_name: str | None = "",
        last_name: str | None = "",
        title: str | None = "",
        company: str | None = "",
        school: str | None = "",
        page: int | None = 1,
        geocode_location: str | None = "",
        current_company: str | None = "",
        profile_language: str | None = "",
        industry: str | None = "",
        service_category: str | None = "",
    ) -> ApiResponse[Any]:
        """
        People Search

        This LinkedIn people-search endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            name: Name or general keyword to search for.
            first_name: First name filter.
            last_name: Last name filter.
            title: Professional title filter.
            company: Company name filter.
            school: School name filter.
            page: Page number, starting from 1.
            geocode_location: LinkedIn geographic location code.
            current_company: LinkedIn current company ID filter.
            profile_language: Profile language filter.
            industry: LinkedIn industry ID filter.
            service_category: LinkedIn service category ID filter.
        """
        return self._get(
            "/api/linkedin/search-user/v1",
            {
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
                "title": title,
                "company": company,
                "school": school,
                "page": page,
                "geocodeLocation": geocode_location,
                "currentCompany": current_company,
                "profileLanguage": profile_language,
                "industry": industry,
                "serviceCategory": service_category,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        username: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's professional background or before requesting published posts.

        Args:
            username: LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack.
        """
        return self._get(
            "/api/linkedin/get-user-detail/v1",
            {
                "username": username,
            },
        )

    def get_company_employees_v1(
        self,
        *,
        company_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Company Employees

        This LinkedIn company-employee endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            company_id: LinkedIn company ID.
            page: Page number, starting from 1.
        """
        return self._get(
            "/api/linkedin/get-company-employees/v1",
            {
                "companyId": company_id,
                "page": page,
            },
        )

    def get_user_posts_v1(
        self,
        *,
        url: str,
        type: str | None = "posts",
        start: int | None = 0,
        pagination_token: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        This LinkedIn user-post endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            url: Full LinkedIn profile URL.
            type: User activity type.  Available Values: - `POSTS`: Posts published by the user - `COMMENTS`: Posts commented on by the user - `REACTIONS`: Posts reacted to by the user
            start: Pagination offset starting from 0, normally increasing by 50.
            pagination_token: Pagination token returned by a previous response.
        """
        return self._get(
            "/api/linkedin/get-user-posts/v1",
            {
                "url": url,
                "type": type,
                "start": start,
                "paginationToken": pagination_token,
            },
        )

    def get_post_reactions_v1(
        self,
        *,
        post_id: str,
        page: int | None = 1,
        type: str | None = "all",
    ) -> ApiResponse[Any]:
        """
        Post Reactions

        This LinkedIn post-reaction-record endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            post_id: LinkedIn post ID.
            page: Page number, starting from 1.
            type: Reaction type filter.  Available Values: - `ALL`: All reaction types - `LIKE`: Like reactions - `PRAISE`: Praise reactions - `EMPATHY`: Empathy reactions - `APPRECIATION`: Appreciation reactions - `INTEREST`: Interest reactions
        """
        return self._get(
            "/api/linkedin/get-post-reactions/v1",
            {
                "postId": post_id,
                "page": page,
                "type": type,
            },
        )

    def get_post_comments_v1(
        self,
        *,
        post_id: str,
        page: int | None = 1,
        sort_order: str | None = "relevance",
        pagination_token: str | None = "",
        share_urn: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        This LinkedIn post-comment endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            post_id: LinkedIn post ID.
            page: Page number, starting from 1.
            sort_order: Comment sort order.  Available Values: - `RELEVANCE`: Sort comments by relevance - `RECENT`: Sort comments from most recent
            pagination_token: Pagination token returned by a previous response.
            share_urn: Optional share URN for a shared post.
        """
        return self._get(
            "/api/linkedin/get-post-comments/v1",
            {
                "postId": post_id,
                "page": page,
                "sortOrder": sort_order,
                "paginationToken": pagination_token,
                "shareUrn": share_urn,
            },
        )

    def search_job_v1(
        self,
        *,
        keyword: str,
        location: str | None = "",
        page: int | None = 1,
        num_pages: int | None = 1,
        geo_id: str | None = "",
        sort_by: str | None = "relevance",
        date_posted: str | None = "all",
        employment_types: list[Any] | None = None,
        seniority_levels: list[Any] | None = None,
        company_id: str | None = "",
        remote_jobs_only: bool | None = False,
        include_details: bool | None = True,
        radius: int | None = None,
        fields: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Job Search

        Searches LinkedIn job postings by keyword with location, posting age, company, employment type, seniority, and pagination filters. Use it to discover recruitment opportunities and research hiring activity.

        Args:
            keyword: Free-form job search keyword.
            location: Free-text location, such as London, United Kingdom.
            page: First page to fetch, from 1 to 100. Each page contains up to 10 jobs.
            num_pages: Number of consecutive pages to fetch, from 1 to 20. The last requested page must not exceed 100.
            geo_id: Numeric LinkedIn geographic location ID. Required when radius is supplied.
            sort_by: Sort order. Date sorting applies to the jobs returned in this response.  Available Values: - `relevance`: Keep relevance ordering - `date`: Sort the returned jobs from newest to oldest
            date_posted: Job posting age filter.  Available Values: - `all`: All posting dates - `today`: Posted within the last 24 hours - `3days`: Posted within the last 72 hours - `week`: Posted within the last 7 days - `month`: Posted within the last 30 days
            employment_types: Comma-separated employment types. Applying this filter enables job details and may return fewer jobs than the requested page size.
            seniority_levels: Comma-separated seniority levels. Applying this filter enables job details and may return fewer jobs than the requested page size.
            company_id: Numeric LinkedIn company ID to restrict the search to one company.
            remote_jobs_only: Return only jobs with an explicit remote marker. This best-effort filter may omit remote jobs.
            include_details: Fetch details for up to 100 jobs per request in addition to search cards. Employment and seniority filters enable details regardless of this value.
            radius: Search radius in kilometres, at least 1. Requires geoId.
            fields: Comma-separated job fields to include. job_id and job_title are always included.
        """
        return self._get(
            "/api/linkedin/search-job/v1",
            {
                "keyword": keyword,
                "location": location,
                "page": page,
                "numPages": num_pages,
                "geoId": geo_id,
                "sortBy": sort_by,
                "datePosted": date_posted,
                "employmentTypes": employment_types,
                "seniorityLevels": seniority_levels,
                "companyId": company_id,
                "remoteJobsOnly": remote_jobs_only,
                "includeDetails": include_details,
                "radius": radius,
                "fields": fields,
            },
        )

    def get_job_detail_v1(
        self,
        *,
        job_id: str,
        fields: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Job Details

        Retrieves LinkedIn job details for up to 20 distinct job identifiers, with optional field projection. Use it to inspect selected postings after a job search; unavailable postings are omitted from the result.

        Args:
            job_id: Comma-separated job IDs returned by job search or raw numeric LinkedIn posting IDs, up to 20 distinct values.
            fields: Comma-separated job fields to include. job_id and job_title are always included.
        """
        return self._get(
            "/api/linkedin/get-job-detail/v1",
            {
                "jobId": job_id,
                "fields": fields,
            },
        )

    def get_company_jobs_v1(
        self,
        *,
        company_id: str | None = "",
        company: str | None = "",
        keyword: str | None = "",
        location: str | None = "",
        page: int | None = 1,
        num_pages: int | None = 1,
        geo_id: str | None = "",
        sort_by: str | None = "relevance",
        date_posted: str | None = "all",
        employment_types: list[Any] | None = None,
        seniority_levels: list[Any] | None = None,
        remote_jobs_only: bool | None = False,
        include_details: bool | None = True,
        radius: int | None = None,
        fields: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Company Jobs

        Retrieves LinkedIn job postings for companies identified by company IDs, vanity names, or company page URLs, with optional keyword, location, posting age, and pagination filters. Use it to track company hiring activity across one or more employers.

        Args:
            company_id: Comma-separated numeric LinkedIn company IDs, up to 10. Supply companyId or company. Companies are matched as a union; a page may contain jobs from only some selected companies.
            company: Comma-separated LinkedIn company vanity names or company page URLs, up to 10. Supply companyId or company. An unknown vanity name fails the request.
            keyword: Optional job keyword to search within the selected companies.
            location: Free-text location, such as London, United Kingdom.
            page: First page to fetch, from 1 to 100. Each page contains up to 10 jobs.
            num_pages: Number of consecutive pages to fetch, from 1 to 20. The last requested page must not exceed 100.
            geo_id: Numeric LinkedIn geographic location ID. Required when radius is supplied.
            sort_by: Sort order. Date sorting applies to the jobs returned in this response.  Available Values: - `relevance`: Keep relevance ordering - `date`: Sort the returned jobs from newest to oldest
            date_posted: Job posting age filter.  Available Values: - `all`: All posting dates - `today`: Posted within the last 24 hours - `3days`: Posted within the last 72 hours - `week`: Posted within the last 7 days - `month`: Posted within the last 30 days
            employment_types: Comma-separated employment types. Applying this filter enables job details and may return fewer jobs than the requested page size.
            seniority_levels: Comma-separated seniority levels. Applying this filter enables job details and may return fewer jobs than the requested page size.
            remote_jobs_only: Return only jobs with an explicit remote marker. This best-effort filter may omit remote jobs.
            include_details: Fetch details for up to 100 jobs per request in addition to search cards. Employment and seniority filters enable details regardless of this value.
            radius: Search radius in kilometres, at least 1. Requires geoId.
            fields: Comma-separated job fields to include. job_id and job_title are always included.
        """
        return self._get(
            "/api/linkedin/get-company-jobs/v1",
            {
                "companyId": company_id,
                "company": company,
                "keyword": keyword,
                "location": location,
                "page": page,
                "numPages": num_pages,
                "geoId": geo_id,
                "sortBy": sort_by,
                "datePosted": date_posted,
                "employmentTypes": employment_types,
                "seniorityLevels": seniority_levels,
                "remoteJobsOnly": remote_jobs_only,
                "includeDetails": include_details,
                "radius": radius,
                "fields": fields,
            },
        )

    def get_company_detail_v1(
        self,
        *,
        company: str,
    ) -> ApiResponse[Any]:
        """
        Company Details

        Retrieves a public LinkedIn company profile by its vanity name or company page URL. Use it to research a company and obtain its company identifier before querying company job postings.

        Args:
            company: LinkedIn company vanity name or company page URL. School pages are not supported.
        """
        return self._get(
            "/api/linkedin/get-company-detail/v1",
            {
                "company": company,
            },
        )
