# Generated from the Seolyticize tool registry. Do not edit by hand:
# regenerate with `pnpm --filter @seolyticize/sdk generate:languages`.
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

READ_ONLY_TOOLS = frozenset({
    "analyse_server_log",
    "batch_domain_metrics",
    "build_disavow_file",
    "estimate_ai_visibility_cost",
    "estimate_cost",
    "explain_keyword_difficulty",
    "export_ai_visibility_data",
    "export_search_console_data",
    "get_agent_readiness",
    "get_ai_visibility",
    "get_ai_visibility_answer",
    "get_ai_visibility_results",
    "get_ai_visibility_runs",
    "get_ai_visibility_setup",
    "get_ai_visibility_trend",
    "get_audit_summary",
    "get_backlink_audit",
    "get_billing",
    "get_bing_performance",
    "get_branding",
    "get_cannibalization",
    "get_click_curve",
    "get_client",
    "get_client_brief",
    "get_client_costs",
    "get_client_integrations",
    "get_connection_link",
    "get_content_decay",
    "get_content_gap",
    "get_costs",
    "get_crawl_status",
    "get_deploy_hook",
    "get_domain_facts",
    "get_domain_technologies",
    "get_entity_pageviews",
    "get_ga4_audience",
    "get_ga4_ecommerce",
    "get_ga4_key_events",
    "get_ga4_landing_pages",
    "get_ga4_measurement_health",
    "get_ga4_overview",
    "get_ga4_page_performance",
    "get_ga4_site_search",
    "get_ga4_traffic_acquisition",
    "get_google_service_account",
    "get_index_coverage",
    "get_indexnow_key",
    "get_keyword_difficulty",
    "get_keyword_gap",
    "get_keyword_list",
    "get_link_checks",
    "get_link_intersect",
    "get_local_visibility",
    "get_low_ctr_queries",
    "get_next_steps",
    "get_opportunities",
    "get_page_issues",
    "get_panel_reach",
    "get_position_distribution",
    "get_rank_history",
    "get_rank_summary",
    "get_run_status",
    "get_search_console_performance",
    "get_search_demand",
    "get_search_opportunities",
    "get_serp_features",
    "get_share_of_voice",
    "get_site_status",
    "get_top_searches",
    "get_url_swaps",
    "get_web_analytics_breakdown",
    "get_web_analytics_setup",
    "get_web_analytics_summary",
    "get_written_report",
    "get_yandex_performance",
    "list_alert_rules",
    "list_clients",
    "list_crawl_issues",
    "list_crawls",
    "list_issue_pages",
    "list_keyword_lists",
    "list_link_prospects",
    "list_local_locations",
    "list_markets",
    "list_projects",
    "list_rank_trackers",
    "list_recent_alerts",
    "list_report_schedules",
    "list_report_templates",
    "list_reports",
    "list_sitemaps",
    "list_tracked_keywords",
    "list_written_reports",
    "page_vitals",
    "striking_distance",
    "whoami",
})

TOOL_COUNT = 199


def _present(values: Dict[str, Any]) -> Dict[str, Any]:
    """Drops arguments left as None, so the server applies its own defaults."""
    return {key: value for key, value in values.items() if value is not None}


class Tools:
    """One method per tool. Every argument is keyword-only, named in snake_case."""

    def call(self, tool: str, input: Optional[Dict[str, Any]] = None) -> Any:  # pragma: no cover
        raise NotImplementedError

    def add_competitors(self, *, client_id: str, tracker_id: str, domains: List[str]) -> Any:
        """Add competitors to a tracker. Adds competitor domains to a rank tracker, so
        share of voice and the competitor comparisons measure them on the same keywords.
        Answers 'compare us with these sites'. Returns the tracker's full competitor
        list. Domains already there are left as they are."""
        return self.call("add_competitors", _present({"clientId": client_id, "trackerId": tracker_id, "domains": domains}))

    def add_keywords_to_list(self, *, list_id: str, keywords: List[Dict[str, Any]]) -> Any:
        """Add keywords to a list. Adds keywords to an existing list. Keywords already on
        it are left alone and counted as already present. Answers 'save these to that
        list'. Location code defaults to 2840 (United States), language to en, engine to
        google."""
        return self.call("add_keywords_to_list", _present({"listId": list_id, "keywords": keywords}))

    def add_link_prospects(self, *, client_id: str, prospects: List[Dict[str, Any]]) -> Any:
        """Add sites to a client's outreach list. Adds linking-site prospects to the
        client's outreach list at the identified stage — typically the domains
        get_link_intersect finds linking to competitors but not the client, with that as
        the reason. A site already on the list is left at its current stage, never
        reset. Answers 'add these sites to our outreach'. Free."""
        return self.call("add_link_prospects", _present({"clientId": client_id, "prospects": prospects}))

    def add_list_to_tracker(self, *, client_id: str, tracker_id: str, list_id: str) -> Any:
        """Track a keyword list. Adds every keyword on a list to one of the client's rank
        trackers. Answers 'start tracking everything on that list'. Keywords for another
        country, language or engine than the tracker reads are skipped and listed with
        the reason, never tracked in the wrong market. Each added keyword is a paid
        lookup on every future run, so quote the tracker with estimate_cost afterwards
        if cost matters; refused when the plan's keyword allowance would be exceeded."""
        return self.call("add_list_to_tracker", _present({"clientId": client_id, "trackerId": tracker_id, "listId": list_id}))

    def add_local_location(self, *, client_id: str, name: str, lat: float, lng: float) -> Any:
        """Add a business location. Adds a business location to a client for local SEO, at
        a latitude and longitude — the centre of every grid scan around it. Answers
        'start tracking this branch in the map pack'. Free."""
        return self.call("add_local_location", _present({"clientId": client_id, "name": name, "lat": lat, "lng": lng}))

    def add_team_member(self, *, email: str, role: Literal["admin", "manager", "analyst", "client_viewer"], client_ids: Optional[List[str]] = None) -> Any:
        """Add someone to the team. Gives an existing Seolyticize account access to the
        agency with a role — admin, manager, analyst or client_viewer — optionally
        limited to some clients. Answers 'give Sam access as an analyst'. The person
        must already have signed up; this never creates an account for them. Refused for
        someone already on the team, and for a client outside the caller's own reach.
        Owners can only be added by an owner, in the app."""
        return self.call("add_team_member", _present({"email": email, "role": role, "clientIds": client_ids}))

    def add_tracked_keywords(self, *, client_id: str, tracker_id: str, terms: List[str]) -> Any:
        """Track keywords. Adds terms to a tracker, ignoring ones already tracked. Answers
        'start tracking these keywords'. Each added term is a paid lookup on every
        future run; refused when the plan's keyword allowance would be exceeded. Safe to
        repeat."""
        return self.call("add_tracked_keywords", _present({"clientId": client_id, "trackerId": tracker_id, "terms": terms}))

    def analyse_server_log(self, *, client_id: str, contents: str) -> Any:
        """Analyse a server access log. Reads a web server access log in combined format
        (nginx's and Apache's default) passed as text, and reports what search and AI
        crawlers spent their visits on: analysis.byBot (hits per crawler), topPaths,
        errorPaths (path, status, hits), wastedOnErrors and wastedOnRedirects (shares of
        crawler requests that returned no content), aiCrawlerShare, totalHits and
        totalBytes. Also linesRead, linesUnparsed (lines in a format it did not
        recognise — many means the wrong format, not a quiet site), humanHits and
        truncated. Up to 64 MB per call; split a bigger log and call once per part.
        Nothing is stored. Answers 'what is Googlebot actually crawling on our site'.
        Free."""
        return self.call("analyse_server_log", _present({"clientId": client_id, "contents": contents}))

    def archive_client(self, *, client_id: str) -> Any:
        """Archive a client. Retires a client: it stops being tracked, crawled and reported
        on, stops counting against the plan, and disappears from lists. History is kept.
        Answers 'we no longer work with this client'. Safe to repeat."""
        return self.call("archive_client", _present({"clientId": client_id}))

    def archive_report(self, *, client_id: str, report_id: str) -> Any:
        """Retire a saved report. Retires a client's saved report so it is no longer sent,
        by schedule or by hand. Answers 'we no longer send this report'. Archived rather
        than deleted: reports already sent to the client stay downloadable. Safe to
        repeat."""
        return self.call("archive_report", _present({"clientId": client_id, "reportId": report_id}))

    def batch_domain_metrics(self, *, domains: List[str]) -> Any:
        """Look up domains in bulk. Authority, keywords, traffic and referring domains for
        any list of domains, managed or not. Answers 'how strong is this site' for
        competitors and prospects."""
        return self.call("batch_domain_metrics", _present({"domains": domains}))

    def build_disavow_file(self, *, entries: List[Dict[str, Any]]) -> Any:
        """Build a disavow file. Builds a Google disavow file from domains and URLs: a
        domain entry disavows every link from that domain, a url entry names one page.
        Answers 'make the disavow file for these links'. Free; nothing is submitted —
        Google takes the file by upload in Search Console, which a person does. Use
        get_backlink_audit to find the links worth disavowing, and have a person review
        every line first: disavowing a good link removes value the client earned.
        Malformed entries are left out rather than written."""
        return self.call("build_disavow_file", _present({"entries": entries}))

    def connect_google_analytics_service_account(self, *, client_id: str, property_id: str) -> Any:
        """Connect GA4 by service account. Connects a client's GA4 property as the agency's
        Google service account, once the property's owner has added that address with
        the Viewer role. Answers 'they added our address in GA4, connect it'. propertyId
        is GA4's numeric property id (Admin → Property details), not a G- measurement
        id. Access is checked with Google first, and refused with the exact steps when
        it is not granted yet. Free."""
        return self.call("connect_google_analytics_service_account", _present({"clientId": client_id, "propertyId": property_id}))

    def connect_search_console_service_account(self, *, client_id: str, property_url: Optional[str] = None) -> Any:
        """Connect Search Console by service account. Connects a client's Search Console
        property as the agency's Google service account (get_google_service_account),
        once the property's owner has added that address as a user. Answers 'they added
        our address, connect Search Console'. Access is checked with Google first: with
        no propertyUrl, the client's site is tried as a Domain property (sc-domain:) and
        then as https:// and https://www. URL-prefix properties, and the first the
        account can read is connected. If none can be read yet, it is refused with the
        exact steps for the owner. Starts the sixteen-month backfill. Free."""
        return self.call("connect_search_console_service_account", _present({"clientId": client_id, "propertyUrl": property_url}))

    def connect_yandex_with_token(self, *, client_id: str, token: str) -> Any:
        """Connect Yandex Webmaster with a token. Connects a client's Yandex Webmaster with
        an OAuth token a person made in their own Yandex app (get_connection_link with
        yandex_webmaster returns the steps), instead of signing in through Seolyticize.
        Answers 'here is the Yandex token, connect it'. Yandex is asked whose token it
        is and the client's site is matched against that account's verified hosts; the
        response says which host matched, or that none did. Works even where this
        deployment has no Yandex sign-in set up. The token is stored sealed and never
        returned. Free."""
        return self.call("connect_yandex_with_token", _present({"clientId": client_id, "token": token}))

    def create_alert_rule(self, *, client_id: str, kind: Literal["rank-drop", "traffic-drop", "new-critical-issues", "backlinks-lost", "site-unreachable"], threshold: int, cooldown_hours: Optional[int] = None, webhook_url: Optional[str] = None, channel: Optional[Literal["slack", "webhook", "email", "telegram"]] = None, email_recipients: Optional[List[str]] = None, telegram_chat_id: Optional[str] = None) -> Any:
        """Create an alert rule. Raises an alert when a client's rankings, traffic, issues
        or backlinks cross a threshold, or the site goes down, and delivers it by
        channel: slack (webhookUrl, Slack's format; the default), webhook (webhookUrl,
        plain JSON), email (emailRecipients, up to ten) or telegram (telegramChatId,
        with the agency's bot from Settings). Webhooks must be https and public. Answers
        'tell me when rankings drop'."""
        return self.call("create_alert_rule", _present({"clientId": client_id, "kind": kind, "threshold": threshold, "cooldownHours": cooldown_hours, "webhookUrl": webhook_url, "channel": channel, "emailRecipients": email_recipients, "telegramChatId": telegram_chat_id}))

    def create_api_key(self, *, name: str, client_id: Optional[str] = None, role: Optional[Literal["client_viewer", "analyst", "manager", "site_admin", "admin"]] = None, expires_in_days: Optional[int] = None, max_cost_usd_per_call: Optional[float] = None) -> Any:
        """Create an API key. Mints an API key, agency-wide or pinned to one client, with a
        role: client_viewer (read-only), analyst, manager, site_admin or admin. Answers
        'give this integration its own key'. For an agent that runs one site, pin it to
        that client with site_admin: full control of that client — connecting consoles,
        crawls, onboarding — and none of the agency's settings, team, keys or billing;
        the key cannot even see other clients. A client-pinned key is at most
        site_admin, and site_admin needs a clientId. expiresInDays makes it stop working
        on its own; maxCostUsdPerCall caps what any one call with it may spend. The key
        is in the response once and can never be shown again. A key cannot be given more
        access than the caller has."""
        return self.call("create_api_key", _present({"name": name, "clientId": client_id, "role": role, "expiresInDays": expires_in_days, "maxCostUsdPerCall": max_cost_usd_per_call}))

    def create_client(self, *, name: str, domain: str, keywords: Optional[List[str]] = None, monthly_budget_usd: Optional[float] = None) -> Any:
        """Create a client. Onboards a client in one step: the client, a project, its site
        and a rank tracker, optionally with keywords to track. Answers 'set up a new
        client'. Refused when the name is taken or the plan's client or keyword
        allowance is used up; every tracked keyword is a paid lookup on every run."""
        return self.call("create_client", _present({"name": name, "domain": domain, "keywords": keywords, "monthlyBudgetUsd": monthly_budget_usd}))

    def create_deploy_hook(self, *, client_id: str, sitemap_url: Optional[str] = None) -> Any:
        """Create a deploy hook. Answers 'tell search engines whenever we deploy'. Makes
        the client's deploy hook: a secret URL the site's pipeline calls after every
        deploy (one curl, or a Netlify/Vercel/Cloudflare Pages/Coolify notification).
        Each call reads the sitemap, compares it with the last one, and submits the new
        and changed pages to IndexNow; the first call records the baseline only. Returns
        the URL once, with how to call it from each platform. Making it again replaces
        the URL. Free."""
        return self.call("create_deploy_hook", _present({"clientId": client_id, "sitemapUrl": sitemap_url}))

    def create_invite_code(self, *, label: str, max_uses: Optional[int] = None, expires_in_days: Optional[int] = None, key_expires_in_days: Optional[int] = None, key_max_cost_usd_per_call: Optional[float] = None) -> Any:
        """Create an invite code for a site's agent. Answers 'let an agent connect its own
        site without our admin key'. Makes a code to hand to the agent that runs one
        site. The agent sends it, with its domain, to POST /api/v1/claim (no key needed)
        and gets back a key pinned to the one new client for that site, with the
        site_admin role: full control of that client, nothing else in the agency. The
        code is in this response once. maxUses (default 1) is how many sites it can
        claim; expiresInDays ends the code, keyExpiresInDays the keys it makes, and
        keyMaxCostUsdPerCall caps what any one call with those keys may spend. Free."""
        return self.call("create_invite_code", _present({"label": label, "maxUses": max_uses, "expiresInDays": expires_in_days, "keyExpiresInDays": key_expires_in_days, "keyMaxCostUsdPerCall": key_max_cost_usd_per_call}))

    def create_keyword_list(self, *, name: str, client_id: Optional[str] = None, keywords: Optional[List[Dict[str, Any]]] = None) -> Any:
        """Create a keyword list. Creates a named keyword list, for one client or for the
        agency, optionally with its first keywords. Answers 'keep these keywords
        somewhere'. A keyword is its words plus a location code, language and engine;
        the same words for another country are a different keyword. Returns created:
        false with the reason when the name is already taken, rather than failing."""
        return self.call("create_keyword_list", _present({"name": name, "clientId": client_id, "keywords": keywords}))

    def create_portal_link(self, *, client_id: str, label: str) -> Any:
        """Create a client portal link. Makes a white-label link that shows one client
        their own dashboard under the agency's name, with no sign-in. Answers 'give the
        client a link to their results'. The full address is in this response once and
        can never be shown again; send it to the client and keep it out of logs. Anyone
        holding it can see that client's results until it is revoked."""
        return self.call("create_portal_link", _present({"clientId": client_id, "label": label}))

    def create_project(self, *, client_id: str, name: str, domain: Optional[str] = None, location_code: Optional[int] = None, language_code: Optional[str] = None) -> Any:
        """Create a project. Adds a project to a client, optionally with a site domain to
        crawl. Answers 'add a second site or market for this client'. The domain is
        written like example.com."""
        return self.call("create_project", _present({"clientId": client_id, "name": name, "domain": domain, "locationCode": location_code, "languageCode": language_code}))

    def create_rank_tracker(self, *, client_id: str, name: str, project_id: Optional[str] = None, domain: Optional[str] = None, engine: Optional[Literal["google", "bing", "youtube", "amazon", "app_store", "yandex", "baidu", "naver", "duckduckgo", "yahoo", "seznam", "google_play"]] = None, device: Optional[Literal["desktop", "mobile", "both"]] = None, frequency: Optional[Literal["daily", "weekly"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None) -> Any:
        """Create a rank tracker. Starts tracking a client's positions on one engine,
        device and locale. Answers 'track this client on Bing too' or 'track mobile
        separately'. Defaults to the client's first project and site domain. Engine and
        locale cannot be changed later — they are part of every keyword's identity — so
        a different market is a new tracker."""
        return self.call("create_rank_tracker", _present({"clientId": client_id, "name": name, "projectId": project_id, "domain": domain, "engine": engine, "device": device, "frequency": frequency, "locationCode": location_code, "languageCode": language_code}))

    def create_report(self, *, client_id: str, title: str, sections: List[Literal["rank-summary", "share-of-voice", "keyword-movers", "backlink-summary", "traffic", "core-web-vitals", "site-health", "audit-summary"]]) -> Any:
        """Create a report. Saves a report for a client from a list of sections; each is
        wired to the client's own tracker and site. Answers 'build a monthly report for
        this client'. Sections the client has nothing for yet are left out. Send it with
        send_report; schedules are set in the app."""
        return self.call("create_report", _present({"clientId": client_id, "title": title, "sections": sections}))

    def delete_alert_rule(self, *, client_id: str, rule_id: str) -> Any:
        """Delete an alert rule. Deletes a rule and every alert it ever fired. Answers
        'remove this alert for good'. To stop it but keep its history, pause it with
        update_alert_rule instead. Safe to repeat."""
        return self.call("delete_alert_rule", _present({"clientId": client_id, "ruleId": rule_id}))

    def delete_keyword_list(self, *, list_id: str) -> Any:
        """Delete a keyword list. Deletes a keyword list and the keywords on it, for good.
        Answers 'get rid of that list'. Keywords a tracker took from the list stay
        tracked."""
        return self.call("delete_keyword_list", _present({"listId": list_id}))

    def delete_rank_tracker(self, *, client_id: str, tracker_id: str) -> Any:
        """Delete a rank tracker. Stops a tracker. Positions it already captured stay in
        reports; no further runs are made or charged. Answers 'stop tracking this'. Safe
        to repeat."""
        return self.call("delete_rank_tracker", _present({"clientId": client_id, "trackerId": tracker_id}))

    def delete_report_schedule(self, *, client_id: str, schedule_id: str) -> Any:
        """Delete a report schedule. Removes a schedule for good: its recipients stop
        receiving that report. Answers 'stop sending this report'. The report itself and
        its past sends are kept. To stop it for a while instead, pause it with
        update_report_schedule."""
        return self.call("delete_report_schedule", _present({"clientId": client_id, "scheduleId": schedule_id}))

    def delete_report_template(self, *, template_id: str, client_id: Optional[str] = None) -> Any:
        """Delete a report template. Permanently deletes one report template. Answers 'we
        no longer use that format'. Reports written to it are kept. Call
        list_report_templates to find its id. Free."""
        return self.call("delete_report_template", _present({"templateId": template_id, "clientId": client_id}))

    def delete_sitemap(self, *, client_id: str, sitemap_url: str) -> Any:
        """Remove a sitemap from Google. Removes a sitemap from the client's Google Search
        Console property. Answers 'stop Google reading this old sitemap'. Same refusals
        as submit_sitemap: only addresses on a site the agency manages, and only once
        sitemap management has been allowed."""
        return self.call("delete_sitemap", _present({"clientId": client_id, "sitemapUrl": sitemap_url}))

    def delete_written_report(self, *, client_id: str, report_id: str) -> Any:
        """Delete a written report. Permanently deletes one written report; its share link
        stops working at once. Answers 'remove that report'. Does not touch data
        reports, templates or anything else. Free."""
        return self.call("delete_written_report", _present({"clientId": client_id, "reportId": report_id}))

    def disconnect_app(self, *, grant_id: str) -> Any:
        """Disconnect an app. Stops a signed-in app working, at once: its access and
        refresh tokens both end. Answers 'remove that assistant's access'. Takes the
        grantId from list_connected_apps. The app can only come back if somebody signs
        in and approves it again. Safe to repeat."""
        return self.call("disconnect_app", _present({"grantId": grant_id}))

    def draft_client_brief(self, *, client_id: str, max_cost_micros: Optional[int] = None) -> Any:
        """Draft the client brief from their website. Reads the client's home page and up
        to four of its about, services, product or pricing pages, and drafts the brief's
        overview, positioning, audience and voice, plus the key pages with what each is
        for. Answers 'set up this client's brief'. Nothing is saved: show the draft to
        the user, correct it, then save what is right with update_client_brief —
        alreadyWritten lists fields the brief already has, which should not be
        overwritten without asking. Says 'Not stated on the site.' where the pages are
        silent, and never names competitors. A paid Claude call charged to the client's
        budget (costMicros reports what it cost). Can spend: pass max_cost_micros to cap
        it."""
        return self.call("draft_client_brief", _present({"clientId": client_id, "maxCostMicros": max_cost_micros}))

    def estimate_ai_visibility_cost(self, *, client_id: str) -> Any:
        """What an AI visibility check costs. Estimates one check and a month at the
        current cadence: questions × assistants answers per run, and the most the Claude
        answers can cost (Seolyticize meters Claude; other assistants bill the agency's
        own accounts at their own prices, so they are counted, not priced). Answers 'how
        much will tracking this cost'. Free."""
        return self.call("estimate_ai_visibility_cost", _present({"clientId": client_id}))

    def estimate_cost(self, *, tool: str, arguments: Optional[Dict[str, Any]] = None) -> Any:
        """Estimate what a call will cost. Quotes the most a tool call can cost before it
        is made, without buying anything. Answers 'how much will this cost'. Pass the
        tool's name and the exact arguments you would call it with; the result lists
        each purchase the call can make with its ceiling, plus monthlyMicros for
        scheduled work. Show the estimate to the user before a paid call, then pass
        estimatedMaxMicros as that call's maxCostMicros so it cannot spend more. Cached
        data costs nothing, so real charges are often lower. Also quotes "rank_tracker":
        a rank tracker's captures (arguments: clientId, trackerId) — per run and per
        month. Free."""
        return self.call("estimate_cost", _present({"tool": tool, "arguments": arguments}))

    def estimate_domain_traffic(self, *, client_id: str, targets: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Estimate search traffic for domains. A vendor's current estimate of monthly
        organic search traffic and ranking keywords for up to 100 domains, bought now.
        Answers 'how much search traffic do these competitors get'. Modelled from
        rankings, not measured visits. batch_domain_metrics reads what is already stored
        for free; use this when those figures are missing or stale. A paid lookup on the
        client's account: quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("estimate_domain_traffic", _present({"clientId": client_id, "targets": targets, "maxCostMicros": max_cost_micros}))

    def explain_keyword_difficulty(self, *, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, keyword_id: Optional[str] = None) -> Any:
        """Why a keyword is as hard as it is. Which first-page results set a keyword's
        difficulty score and which make it harder than the score suggests: each result's
        referring domains and role (sets the median, above it, below it, or unscored for
        lack of link data), the strongest and weakest result, the domain authority
        beside each, and a one-paragraph summary. Answers 'why is this keyword a 47' so
        the number can be checked rather than trusted. Read from the archive and our
        link graph; buys nothing, and a keyword never captured is reported unscored."""
        return self.call("explain_keyword_difficulty", _present({"term": term, "locationCode": location_code, "languageCode": language_code, "keywordId": keyword_id}))

    def explore_ai_prompt(self, *, prompt: str, client_id: Optional[str] = None, engines: Optional[List[Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"]]] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Ask assistants one question now. Asks one question live on the chosen assistants
        (claude, and any the agency has its own API key for) and returns each answer's
        text, citations, and — when clientId is given — which tracked brands it named.
        Nothing is stored; use it to see what assistants say before tracking a question,
        or to look up how they describe a brand. Answers 'what does ChatGPT say about
        this'. Claude is metered (meteredMicros); others bill the agency's own accounts.
        Can spend: pass max_cost_micros to cap it."""
        return self.call("explore_ai_prompt", _present({"clientId": client_id, "prompt": prompt, "engines": engines, "maxCostMicros": max_cost_micros}))

    def export_ai_visibility_data(self, *, client_id: str, days: Optional[int] = None, include: Optional[Literal["mentions", "answers"]] = None) -> Any:
        """Export AI visibility data. CSV of the last N days (default 90): include
        "mentions" for one row per answer and brand (named, position, cited), or
        "answers" for the full answer text and citations (up to 2,000 answers). Returns
        rows and csv. Answers 'give me the raw data for a deck'. Free."""
        return self.call("export_ai_visibility_data", _present({"clientId": client_id, "days": days, "include": include}))

    def export_search_console_data(self, *, client_id: str, from_: str, to: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, country: Optional[str] = None, device: Optional[Literal["DESKTOP", "MOBILE", "TABLET"]] = None, dimension: Optional[Literal["query", "page"]] = None) -> Any:
        """Export Search Console queries or pages as CSV. Google Search Console queries or
        pages (dimension) for a search type, date range, and optionally one country and
        device, as CSV with clicks, impressions, click-through rate and average position
        — up to 5,000 rows. Returns filename, rows and csv. Cells a spreadsheet would
        run as formulas are neutralised. Answers 'give me the query data in a
        spreadsheet'. Free."""
        return self.call("export_search_console_data", _present({"clientId": client_id, "searchType": search_type, "from": from_, "to": to, "country": country, "device": device, "dimension": dimension}))

    def find_serp_competitors(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, limit: Optional[int] = None, exclude: Optional[List[str]] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Who competes across a keyword set. Finds the domains that rank across a set of
        keywords (up to 200) in one market: visibility (share of the keywords they hold
        in the top ten), keyword count, average position and estimated traffic. Answers
        'who are our real search competitors for these terms'. List the client's own
        domain in exclude. One purchase per call. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("find_serp_competitors", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "limit": limit, "exclude": exclude, "maxCostMicros": max_cost_micros}))

    def get_agent_readiness(self, *, client_id: str) -> Any:
        """Get agent readiness. Whether the client's site can be read and cited by AI
        assistants — crawler access, rendering, structured data. Answers 'why are
        assistants not citing us'."""
        return self.call("get_agent_readiness", _present({"clientId": client_id}))

    def get_ai_visibility(self, *, client_id: str) -> Any:
        """Get AI assistant visibility. How often the client's brand appears in AI
        assistant answers versus competitors, and what kind of pages those answers were
        built from. Answers 'are we visible in ChatGPT, Copilot, Gemini and Claude' and
        'what do we have to be on to get cited'."""
        return self.call("get_ai_visibility", _present({"clientId": client_id}))

    def get_ai_visibility_answer(self, *, client_id: str, prompt_id: str, model: Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"], captured_at: str) -> Any:
        """Read one AI answer in full. The full text one assistant gave to one question in
        one check, with the pages it cited and where each tracked brand appears in it.
        found is false when that answer was never captured or has aged out (answers are
        kept 13 months). Answers 'what exactly did ChatGPT say'. Free."""
        return self.call("get_ai_visibility_answer", _present({"clientId": client_id, "promptId": prompt_id, "model": model, "capturedAt": captured_at}))

    def get_ai_visibility_results(self, *, client_id: str, captured_at: Optional[str] = None) -> Any:
        """AI visibility results, answer by answer. One check (the latest unless capturedAt
        names one from get_ai_visibility_runs), as a row per question and assistant:
        whether the client was named, where in the answer (character offset; earlier is
        more prominent), whether its site was cited, and which other brands were named,
        in order. Answers 'which questions are we missing from'. Free."""
        return self.call("get_ai_visibility_results", _present({"clientId": client_id, "capturedAt": captured_at}))

    def get_ai_visibility_runs(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """AI visibility checks so far. Lists the client's checks, newest first: when, how
        many answers, which assistants, and in how many the client's own brand was named
        (mentionRate; null when no brand is marked as the client's). Answers 'when did
        we last check, and how did it go'. Free."""
        return self.call("get_ai_visibility_runs", _present({"clientId": client_id, "limit": limit}))

    def get_ai_visibility_setup(self, *, client_id: str) -> Any:
        """AI visibility setup. Reads what is tracked for a client: the questions (with
        their market), the brands looked for (which one is the client's own), the
        schedule (cadence, which assistants, last run), and which assistants this agency
        can ask at all and how (its own key or its proxy pool). Answers 'what are we
        measuring in AI assistants'. Free."""
        return self.call("get_ai_visibility_setup", _present({"clientId": client_id}))

    def get_ai_visibility_trend(self, *, client_id: str, days: Optional[int] = None) -> Any:
        """Is AI visibility improving. The client's own mention rate over the last N days
        (default 28) against the N days before, overall and per assistant, counted by
        answer, with how many answers each side rests on. Answers 'are we being
        recommended more than last month'. Free."""
        return self.call("get_ai_visibility_trend", _present({"clientId": client_id, "days": days}))

    def get_audit_summary(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """Get site audit summary. Technical issues one crawl found, grouped by rule: each
        with its name, severity, category, how many pages it affects and howToFix.
        Answers 'what is broken on the site'. crawlId defaults to the latest completed
        crawl. Then list_issue_pages shows which pages an issue is on."""
        return self.call("get_audit_summary", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_backlink_audit(self, *, client_id: str, money_terms: Optional[List[str]] = None) -> Any:
        """Audit a client's backlinks. The client's backlinks, each scored from signals an
        agency can check — source authority, how many sites the source links out to, and
        the anchor — with a verdict of healthy, review or toxic and the reasons. Also
        the top referring domains, the top anchors, and the links our own crawler found
        (page-level, ours alone). Brand terms come from the client's name and domain, so
        a branded anchor is not read as paid; pass moneyTerms (commercial phrases such
        as 'cheap flights') to flag exact-match anchors. Answers 'are any of our links a
        problem'. 'review' means look at it, not that it is bad. domain is null when the
        client has no site yet. Free."""
        return self.call("get_backlink_audit", _present({"clientId": client_id, "moneyTerms": money_terms}))

    def get_backlink_spam_scores(self, *, client_id: str, domains: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """The vendor's spam scores for linking sites. The data vendor's own spam score
        (0–100, null when it has none) for each domain you pass — usually the sources
        from get_backlink_audit. A second opinion beside ours: a link both call bad is
        one to act on. Paid, one purchase per call however many domains (up to 1000):
        quote it with estimate_cost and get the user's go-ahead first. Answers 'what
        does the vendor think of these links'. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("get_backlink_spam_scores", _present({"clientId": client_id, "domains": domains, "maxCostMicros": max_cost_micros}))

    def get_billing(self) -> Any:
        """Read the agency's plan. The agency's plan, its limits, how many clients it uses,
        and the subscription's status and renewal date. Answers 'how many more clients
        can we add'. `configured` is false where this deployment sells nothing — every
        agency is on the trial plan then, and that is not an error."""
        return self.call("get_billing", {})

    def get_billing_link(self, *, plan: Optional[Literal["studio", "agency", "network"]] = None) -> Any:
        """Get a link to pay or manage the plan. A Stripe address for a person to open:
        checkout for a plan (studio, agency or network), or — with no plan, for an
        agency already paying — the portal where cards, invoices and cancellation live.
        Answers 'upgrade our plan'. An agent cannot pay; hand the address to a person.
        Refused where this deployment has no billing set up."""
        return self.call("get_billing_link", _present({"plan": plan}))

    def get_bing_performance(self, *, client_id: str) -> Any:
        """What Bing Webmaster Tools reports. The client's site as Bing reports it, on the
        agency's Webmaster Tools key: daily clicks and impressions, page and query
        stats, crawl stats (pages crawled, in index, errors by status), crawl issues per
        URL, sitemaps and feeds, and the URL submission quota. Answers 'how is this site
        doing in Bing'. These are Bing's numbers about Bing's searchers and must never
        be added to Google's. Each part is separately present or failed; connected is
        false when the agency has no Bing key."""
        return self.call("get_bing_performance", _present({"clientId": client_id}))

    def get_brand_mentions(self, *, client_id: str, keyword: str, max_cost_micros: Optional[int] = None) -> Any:
        """Find recent mentions of a brand or phrase. Who has written about a brand or
        phrase lately — the page, its title and snippet, when it was published, and how
        it read (positive, negative or neutral) — one result per publishing domain, up
        to 50. Answers 'who is talking about us' and finds unlinked mentions worth
        asking for a link. A paid lookup on the client's account: quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_brand_mentions", _present({"clientId": client_id, "keyword": keyword, "maxCostMicros": max_cost_micros}))

    def get_branding(self) -> Any:
        """Read the agency's branding. The agency's name, logo address and primary colour:
        what clients see on reports and portal links. Answers 'what will this report
        look like to the client'. Empty strings where nothing is set."""
        return self.call("get_branding", {})

    def get_cannibalization(self, *, client_id: str) -> Any:
        """Get cannibalization. Keywords where several of the client's own pages compete in
        the same result. Answers 'where are we competing with ourselves'."""
        return self.call("get_cannibalization", _present({"clientId": client_id}))

    def get_click_curve(self, *, engine: Optional[str] = None, market: Optional[str] = None, query: Optional[str] = None) -> Any:
        """How clicks fall away down a results page. The share of clicks each position
        took, as the panel observed it — for one query, or across a whole market.
        Answers 'what is a position actually worth here' with a measurement rather than
        a published average. Positions too few people clicked are withheld, so the
        shares deliberately do not add up to one: the rest of the page is unmeasured,
        not empty."""
        return self.call("get_click_curve", _present({"engine": engine, "market": market, "query": query}))

    def get_client(self, *, client_id: str) -> Any:
        """Get a client. One client's settings with its projects, sites and rank trackers.
        Answers 'what is set up for this client' — use it to find tracker, project and
        site ids before changing anything."""
        return self.call("get_client", _present({"clientId": client_id}))

    def get_client_brief(self, *, client_id: str) -> Any:
        """Read the client brief. Reads what the agency knows about a client: overview,
        current goal, positioning, audience, writing voice, competitors, key pages,
        custom sections, and the research log (newest first). Answers 'what do we know
        about this client'. Read it before researching, writing or reporting for a
        client, so the work matches the business and builds on earlier findings. Fields
        nobody has written are null, not empty. Free."""
        return self.call("get_client_brief", _present({"clientId": client_id}))

    def get_client_costs(self, *, client_id: str, since_days: Optional[int] = None) -> Any:
        """Vendor spend for one client. What one client's data cost over recent days, by
        operation, with request counts. Answers 'what are we paying for on this
        account'. Amounts are US dollars."""
        return self.call("get_client_costs", _present({"clientId": client_id, "sinceDays": since_days}))

    def get_client_integrations(self, *, client_id: str) -> Any:
        """Which consoles are connected for a client. Whether a client's Google Search
        Console and Google Analytics properties are connected and syncing, with the last
        sync error, and whether IndexNow is set up. Answers 'is Search Console connected
        for this client'. Never returns tokens."""
        return self.call("get_client_integrations", _present({"clientId": client_id}))

    def get_connection_link(self, *, client_id: str, service: Literal["search_console", "search_console_sitemaps", "google_analytics", "yandex_webmaster", "google_business_profile"], property_url: Optional[str] = None, ga4_property_id: Optional[str] = None, location_id: Optional[str] = None) -> Any:
        """Get a link for a person to connect a service. The link a PERSON must open to
        connect one of a client's accounts — Google Search Console (search_console),
        Search Console sitemap management (search_console_sitemaps), Google Analytics 4
        (google_analytics), Yandex Webmaster (yandex_webmaster) or a Google Business
        Profile listing (google_business_profile) — with what they will be asked to
        approve and what is connected now. Answers 'connect Search Console for this
        client' and 'did the connection work'. An agent cannot complete these itself:
        the account owner signs in to that service and grants access. Give the url and
        the steps to your human, then call this again to check state. The person must be
        signed in to Seolyticize with permission to manage the client. google_analytics
        needs ga4PropertyId (the numeric property id, not a G- measurement id);
        google_business_profile needs locationId; search_console takes an optional
        propertyUrl (default: the client's site, https://domain/; a Domain property is
        sc-domain:example.com). Free."""
        return self.call("get_connection_link", _present({"clientId": client_id, "service": service, "propertyUrl": property_url, "ga4PropertyId": ga4_property_id, "locationId": location_id}))

    def get_content_decay(self, *, client_id: str) -> Any:
        """Get decaying content. Pages losing the traffic they used to earn, over
        consecutive periods. Answers 'what should we refresh'."""
        return self.call("get_content_decay", _present({"clientId": client_id}))

    def get_content_gap(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get content gap. Competitor pages that own a cluster of keywords the client does
        not cover. Answers 'what page should we build next' — use this rather than
        keyword gap when planning content."""
        return self.call("get_content_gap", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_costs(self, *, since_days: Optional[int] = None) -> Any:
        """Vendor spend by client. What the agency spent on data vendors per client over
        recent days, with request counts. Answers 'which clients cost us the most'.
        Amounts are US dollars."""
        return self.call("get_costs", _present({"sinceDays": since_days}))

    def get_crawl_status(self, *, client_id: str, crawl_id: str) -> Any:
        """Get crawl status. Whether one crawl is running, complete or failed, with page
        and issue counts and the failure reason. Answers 'has the audit finished'."""
        return self.call("get_crawl_status", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_deploy_hook(self, *, client_id: str) -> Any:
        """Get the deploy hook's status. Answers 'did the last deploy notify search
        engines'. Whether the client has a deploy hook, how many sitemap pages it knows,
        and what its last call did. Never the URL itself. Free."""
        return self.call("get_deploy_hook", _present({"clientId": client_id}))

    def get_domain_facts(self, *, domain: str, max_cost_micros: Optional[int] = None) -> Any:
        """What the open web says about a domain. Registration date and registrar from the
        registry, position on the Tranco top-sites list, when the Internet Archive first
        captured it, and the subdomains its certificates have announced. Answers 'how
        old and how big is this, and what else is on it' for any domain, free and
        without touching a vendor. Each figure is absent far more often than present,
        and an absence is never a zero: no registry record, not in the top million,
        never archived. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_domain_facts", _present({"domain": domain, "maxCostMicros": max_cost_micros}))

    def get_domain_technologies(self, *, domain: str) -> Any:
        """See what a domain is built with. The technologies our own crawler detected on
        any domain — CMS, analytics, commerce, CDN and so on — with the version most
        pages showed and how many pages showed it, as of the day it was last crawled.
        Answers 'what is this site built on'. Free. Null when our crawler has never
        fetched the domain, which says nothing about what it runs."""
        return self.call("get_domain_technologies", _present({"domain": domain}))

    def get_entity_pageviews(self, *, entity: str, from_: str, to: str, language: Optional[str] = None, granularity: Optional[Literal["daily", "monthly"]] = None) -> Any:
        """How many people looked a brand or topic up. Wikipedia article views for a brand
        or topic over a period, daily or monthly. Answers 'is interest in this name
        growing' with a complete count published by Wikimedia rather than a vendor's
        model or a panel sample. Returns nothing at all when Wikipedia has no article,
        which is the case for most small brands — and says which article it counted,
        because the closest article is not always the brand's own."""
        return self.call("get_entity_pageviews", _present({"entity": entity, "language": language, "granularity": granularity, "from": from_, "to": to}))

    def get_ga4_audience(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, by: Optional[Literal["device", "country", "newVsReturning"]] = None, channel: Optional[Literal["organic", "all"]] = None) -> Any:
        """Who arrives (GA4). Users, sessions, engaged sessions and key events by device,
        country, or new versus returning (by), organic search by default. Answers 'is
        mobile or desktop converting, which countries'. Rows carry key, current (metrics
        by name) and previous (null when compare is false, metrics null where that
        period had no row). Also period, previousPeriod, currency, thresholded and
        folded. Refuses with a sentence when the client has not connected a GA4
        property. Free."""
        return self.call("get_ga4_audience", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "by": by, "channel": channel}))

    def get_ga4_ecommerce(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, by: Optional[Literal["item", "landingPage"]] = None) -> Any:
        """Shop performance (GA4). Item views, add-to-carts, purchases and item revenue by
        item, or transactions and purchase revenue by organic landing page (by
        "landingPage"). activity is "detected" or "none" — none means the property sends
        no ecommerce events for the period, not that nothing sold. Answers 'what is
        selling, and from which pages'. Rows carry key, current (metrics by name) and
        previous (null when compare is false, metrics null where that period had no
        row). Also period, previousPeriod, currency, thresholded and folded. Refuses
        with a sentence when the client has not connected a GA4 property. Free."""
        return self.call("get_ga4_ecommerce", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "by": by}))

    def get_ga4_key_events(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, by: Optional[Literal["event", "landingPage"]] = None) -> Any:
        """Key events (GA4). Counts of the property's key events (what used to be
        conversions) by event name, or by the organic landing page that led to them (by
        "landingPage"). Answers 'what are visitors converting on'. Rows carry key,
        current (metrics by name) and previous (null when compare is false, metrics null
        where that period had no row). Also period, previousPeriod, currency,
        thresholded and folded. Refuses with a sentence when the client has not
        connected a GA4 property. Free."""
        return self.call("get_ga4_key_events", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "by": by}))

    def get_ga4_landing_pages(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all"]] = None) -> Any:
        """What landing pages did (GA4). Sessions, engaged sessions, engagement rate, key
        events, transactions and revenue by landing page, organic search by default.
        Answers 'which pages search sends people to, and what they did there'. Rows
        carry key, current (metrics by name) and previous (null when compare is false,
        metrics null where that period had no row). Also period, previousPeriod,
        currency, thresholded and folded. Refuses with a sentence when the client has
        not connected a GA4 property. Free."""
        return self.call("get_ga4_landing_pages", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "channel": channel}))

    def get_ga4_measurement_health(self, *, client_id: str) -> Any:
        """Is the property measuring properly (GA4). Checks the connected property's setup:
        web data streams and measurement ids, enhanced measurement per stream (scrolls,
        outbound clicks, site search, forms, downloads), marked key events, custom
        dimensions and metrics, and the last day with sessions. findings lists problems,
        warnings and notes in plain words; a part that could not be read is reported as
        unread, not as fine. Answers 'can we trust this client's Analytics'. Refuses
        with a sentence when the client has not connected a GA4 property. Free."""
        return self.call("get_ga4_measurement_health", _present({"clientId": client_id}))

    def get_ga4_overview(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all"]] = None) -> Any:
        """Is organic traffic growing (GA4). Top-line sessions, users, engaged sessions,
        engagement rate, key events, transactions and revenue for organic search
        (channel "all" for every channel), against the previous period, plus a daily
        sessions and key-events line. Answers 'is organic traffic improving'. total
        holds the figures. Rows carry key, current (metrics by name) and previous (null
        when compare is false, metrics null where that period had no row). Also period,
        previousPeriod, currency, thresholded and folded. Refuses with a sentence when
        the client has not connected a GA4 property. Free."""
        return self.call("get_ga4_overview", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "channel": channel}))

    def get_ga4_page_performance(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all"]] = None) -> Any:
        """Page views and engagement (GA4). Views, users, total engagement time in seconds
        and key events by page path, organic search by default (channel "all" for every
        channel). Answers 'which pages hold attention'. Rows carry key, current (metrics
        by name) and previous (null when compare is false, metrics null where that
        period had no row). Also period, previousPeriod, currency, thresholded and
        folded. Refuses with a sentence when the client has not connected a GA4
        property. Free."""
        return self.call("get_ga4_page_performance", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "channel": channel}))

    def get_ga4_site_search(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None) -> Any:
        """What visitors search for on the site (GA4). Terms people typed into the site's
        own search, with searches and users. measured is false when the property records
        no site search (enhanced measurement off, or no search box). Answers 'what are
        people looking for that the site does not surface'. Rows carry key, current
        (metrics by name) and previous (null when compare is false, metrics null where
        that period had no row). Also period, previousPeriod, currency, thresholded and
        folded. Refuses with a sentence when the client has not connected a GA4
        property. Free."""
        return self.call("get_ga4_site_search", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit}))

    def get_ga4_traffic_acquisition(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, group_by: Optional[Literal["channel", "sourceMedium", "campaign"]] = None) -> Any:
        """Where traffic comes from (GA4). Sessions, users, engaged sessions, key events,
        transactions and revenue by channel group, source/medium or campaign (groupBy),
        against the previous period. Answers 'which channels grew or fell'. Rows carry
        key, current (metrics by name) and previous (null when compare is false, metrics
        null where that period had no row). Also period, previousPeriod, currency,
        thresholded and folded. Refuses with a sentence when the client has not
        connected a GA4 property. Free."""
        return self.call("get_ga4_traffic_acquisition", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "groupBy": group_by}))

    def get_google_service_account(self) -> Any:
        """Get the agency's Google service account. The email address of the agency's own
        Google service account, made the first time it is asked for. Answers 'what do I
        add in Search Console so we can connect without signing in'. A client's property
        owner adds this address as a user — Search Console: Settings → Users and
        permissions, Restricted; GA4: Admin → Property access management, Viewer — and
        then connect_search_console_service_account or
        connect_google_analytics_service_account connects it with no Google sign-in. The
        address is the agency's alone; give it to your human to pass on. Free."""
        return self.call("get_google_service_account", {})

    def get_index_coverage(self, *, client_id: str) -> Any:
        """Which of the client's pages Google has indexed. The newest URL Inspection
        verdict for every page of the client's site that has been inspected, grouped by
        verdict and by Google's coverage state, with pages whose Google-chosen canonical
        differs from their own. Answers 'how much of this site is in Google, and what is
        keeping the rest out'. Covers inspected pages only — Search Console's own
        indexing report has no API — and says how many that is and how many are still
        queued."""
        return self.call("get_index_coverage", _present({"clientId": client_id}))

    def get_indexnow_key(self, *, client_id: str) -> Any:
        """Get the IndexNow key. The client's IndexNow key, the file the site must serve
        for it, and whether that file has been verified. Lists what submit_indexnow
        needs in place. A null key means none has been issued yet: use
        issue_indexnow_key."""
        return self.call("get_indexnow_key", _present({"clientId": client_id}))

    def get_keyword_difficulty(self, *, client_id: str, keyword_ids: List[str]) -> Any:
        """Get keyword difficulty. How hard the first page looks for given keywords, scored
        from how many domains link to the pages already ranking there. Answers 'is this
        term worth going after'. Null where too few results have link data to judge."""
        return self.call("get_keyword_difficulty", _present({"clientId": client_id, "keywordIds": keyword_ids}))

    def get_keyword_gap(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get keyword gap. Keywords competitors rank for that the client does not, sized
        by the clicks available. Answers 'which terms are we missing'."""
        return self.call("get_keyword_gap", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_keyword_list(self, *, list_id: str) -> Any:
        """Read a keyword list. Every keyword in one list (by listId from
        list_keyword_lists): the term, its market, language and engine, its keywordId,
        and its note. Answers 'what is on this list'. Free."""
        return self.call("get_keyword_list", _present({"listId": list_id}))

    def get_keyword_trends(self, *, client_id: str, terms: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Get Google Trends interest for terms. Interest over time from Google Trends for
        up to five terms in the United States, each on a 0–100 scale relative to its own
        peak — so it shows when people care, not how many. Answers 'is this seasonal'
        and 'is this growing'. Different from get_search_demand, which counts people in
        our own panel. A paid lookup on the client's account: quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_keyword_trends", _present({"clientId": client_id, "terms": terms, "maxCostMicros": max_cost_micros}))

    def get_link_checks(self, *, client_id: str) -> Any:
        """Do the linking pages still link?. What our own crawler last saw on each page
        said to link to the client: live (the link is there), lost (the page no longer
        links) or unknown (the page could not be read), with counts. Read from the last
        check, never fetched now. Answers 'which links have we lost'. Run recheck_links
        to check again. Free."""
        return self.call("get_link_checks", _present({"clientId": client_id}))

    def get_link_intersect(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get link prospects. Sites linking to the client's competitors but not to the
        client. Answers 'who should we approach for links'."""
        return self.call("get_link_intersect", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_live_serps(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, engine: Optional[Literal["google", "bing", "youtube", "amazon", "yandex", "baidu", "naver", "duckduckgo", "yahoo", "seznam", "app_store", "google_play"]] = None, device: Optional[Literal["desktop", "mobile"]] = None, top: Optional[int] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Read several results pages now. Reads the live results page for up to 10
        keywords in one market and engine (Google by default), and returns each page's
        top results (position, type, domain, url, title) and the search features on it.
        Answers 'who ranks for these right now'. Each keyword is one purchase, made in
        turn; one that fails is reported and the rest still return; maxCostMicros stops
        before the purchase that would pass it. Quote with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_live_serps", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "engine": engine, "device": device, "top": top, "maxCostMicros": max_cost_micros}))

    def get_local_visibility(self, *, client_id: str, location_id: str, term: str) -> Any:
        """Map-pack visibility and reviews for a location. The latest grid scan for a
        search term at one location — the map-pack position at every point, and the
        share of points ranking in the top 3 and top 10 — plus an analysis of the
        location's reviews (rating, volume, recency, response rate). Answers 'where in
        town do we show up for this search'. scanned is false when that term has never
        been scanned there: no grid, rather than a grid of blanks that would read as
        invisible everywhere. Free."""
        return self.call("get_local_visibility", _present({"clientId": client_id, "locationId": location_id, "term": term}))

    def get_low_ctr_queries(self, *, client_id: str, days: Optional[int] = None, min_impressions: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Queries losing clicks to their snippet. Search Console queries on page one
        (positions 1–10) with enough impressions where far fewer people click than that
        position normally earns (under half the click curve's rate): actual and expected
        click-through rate and the clicks missed, worst first. Answers 'which titles and
        descriptions should we rewrite'. Check get_serp_features first — an AI overview
        or map pack above the result also lowers clicks. Free."""
        return self.call("get_low_ctr_queries", _present({"clientId": client_id, "days": days, "minImpressions": min_impressions, "limit": limit}))

    def get_next_steps(self, *, client_id: str) -> Any:
        """What to do next for a site. Answers 'what is left to do for this site, and what
        call does it'. The onboarding checklist with live status — done, todo, in
        progress, failed or blocked and why — each with the exact tool and arguments to
        call next, then, once the site is set up, the weekly loop's calls with their
        arguments. Reads only; changes nothing. Free."""
        return self.call("get_next_steps", _present({"clientId": client_id}))

    def get_opportunities(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """Everything worth working on, in one call. Gathers the four kinds of opportunity
        from stored data: strikingDistance (pages around positions 4–20 by extra
        clicks), lowCtr (page-one queries losing clicks to their snippet), contentDecay
        (pages losing clicks), and cannibalization (pages splitting one query). Each
        part is a section with data or an error — an unread part is not an empty one.
        Answers 'what should we work on for this client'. Use the individual tools for
        detail. Free."""
        return self.call("get_opportunities", _present({"clientId": client_id, "limit": limit}))

    def get_page_issues(self, *, client_id: str, url: str, crawl_id: Optional[str] = None) -> Any:
        """Get every issue on one page. Lists every issue a crawl found on one page, with
        severity, message and howToFix. Answers 'what is wrong with this page' and,
        after a fix and a new crawl, 'is it fixed'. crawlId defaults to the latest
        completed crawl. Free."""
        return self.call("get_page_issues", _present({"clientId": client_id, "url": url, "crawlId": crawl_id}))

    def get_panel_reach(self, *, hosts: List[str], from_: str, to: str) -> Any:
        """Get panel reach. How many panel members visited given hosts over a period, and
        how often. Answers 'what did real people actually do', as far as the panel saw.
        Returns the panelist count alongside the visits so a thin panel is visibly thin
        rather than quietly wrong."""
        return self.call("get_panel_reach", _present({"hosts": hosts, "from": from_, "to": to}))

    def get_position_distribution(self, *, client_id: str, tracker_id: str, days: Optional[int] = None, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get position distribution. How a tracker's keywords spread across positions 1-3,
        4-10, 11-20, 21-50 and 51-100 each day, with average position and visibility,
        per device. Answers 'how many keywords are on page one, and is that growing'.
        Keywords read and not found are counted as not ranking, apart from every band;
        keywords not read that day are counted as not captured. The average is over
        ranking keywords only."""
        return self.call("get_position_distribution", _present({"clientId": client_id, "trackerId": tracker_id, "days": days, "device": device}))

    def get_rank_history(self, *, client_id: str, tracker_id: str, keyword_ids: Optional[List[str]] = None, days: Optional[int] = None, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get rank history. Day-by-day positions for a tracker's keywords, each day with
        the page that ranked and the search features on the page — and which of those
        the client held. Answers 'how has this keyword moved, and with which page'.
        Mobile and desktop are separate series. A null position means the page was read
        and the client was not on it; a missing day means nobody read the page that day.
        Neither is a zero."""
        return self.call("get_rank_history", _present({"clientId": client_id, "trackerId": tracker_id, "keywordIds": keyword_ids, "days": days, "device": device}))

    def get_rank_summary(self, *, client_id: str, tracker_id: str) -> Any:
        """Get rank summary. How many tracked keywords improved, declined or held for a
        client, with the average position. Answers 'are rankings getting better'."""
        return self.call("get_rank_summary", _present({"clientId": client_id, "trackerId": tracker_id}))

    def get_run_status(self, *, client_id: str, job: Literal["rank", "domain"], run_id: str) -> Any:
        """Get the status of a run. How a run started with refresh_rankings or
        refresh_domain_data is going: running, done or failed, and — when it failed or
        captured only some keywords — the reason, written for an agency to act on (a
        missing vendor key, an unreachable site). Answers 'did that capture work'. A run
        id that is not this client's, or that has aged out, reads as unknown."""
        return self.call("get_run_status", _present({"clientId": client_id, "job": job, "runId": run_id}))

    def get_search_console_performance(self, *, client_id: str, from_: str, to: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, country: Optional[str] = None, device: Optional[Literal["DESKTOP", "MOBILE", "TABLET"]] = None, dimensions: Optional[List[Literal["date", "query", "page", "country", "device"]]] = None, page: Optional[str] = None, query: Optional[str] = None) -> Any:
        """What Google Search Console measured. Clicks, impressions and position from the
        client's own Google Search Console, for one search type (web, image, video,
        news, discover, googleNews) over a date range, optionally filtered to one
        country (ISO 3166-1 alpha-3, e.g. gbr) and one device. Ask for any of the
        dimensions date, query, page, country and device; asking for both page and query
        returns the page-by-query drill-down, which has no country or device split.
        Answers 'what did this site actually earn in Google'. Discover and Google News
        have no queries and no position. Days Google is still counting are marked
        provisional. Returns a refusal with a reason when Search Console is not
        connected or a filter does not apply."""
        return self.call("get_search_console_performance", _present({"clientId": client_id, "searchType": search_type, "from": from_, "to": to, "country": country, "device": device, "dimensions": dimensions, "page": page, "query": query}))

    def get_search_demand(self, *, query: str, market: str, since: str) -> Any:
        """What the panel saw people search for. How many people in the panel searched a
        term, and how often, in one market. Answers 'do real people actually search
        this' — a reading from people rather than a vendor's model. Returns nothing at
        all when too few people searched it, because a term seen by two panelists is
        those two people rather than a measurement."""
        return self.call("get_search_demand", _present({"query": query, "market": market, "since": since}))

    def get_search_opportunities(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None) -> Any:
        """Pages worth an edit first (Search Console × GA4). Joins Search Console pages
        ranking around positions 4–20 with what their organic visitors do in GA4 over
        the same window, and ranks them by projected revenue, then projected key events,
        then extra clicks. Each row: page, extraClicks (from the click curve at third
        place), its top queries, the page's organic sessions, key event rate and revenue
        per session (analytics null where GA4 has no row for it — unknown, not
        worthless), and the projections. searchConsole is false when the client has no
        site or console data. Answers 'which page should we improve first'. Refuses with
        a sentence when the client has not connected a GA4 property. Free."""
        return self.call("get_search_opportunities", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit}))

    def get_serp_features(self, *, client_id: str, tracker_id: str, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get SERP features. Which search features — featured snippet, AI Overview, local
        pack, video, People Also Ask and others — appeared on each tracked keyword's
        latest page, and which the client holds, with totals per feature. Answers 'which
        snippets and overviews do we own'. Features are null for a capture whose source
        did not report them, which is not the same as a page with none."""
        return self.call("get_serp_features", _present({"clientId": client_id, "trackerId": tracker_id, "device": device}))

    def get_share_of_voice(self, *, client_id: str, tracker_id: str) -> Any:
        """Get share of voice. The client's share of available search clicks across its
        tracked keywords, alongside competitors. Answers 'how much of the market do we
        hold'."""
        return self.call("get_share_of_voice", _present({"clientId": client_id, "trackerId": tracker_id}))

    def get_site_status(self, *, client_id: str) -> Any:
        """Site verification and connection status. For a client's sites: whether the
        IndexNow key file has been published and verified, which Search Console
        properties are connected and syncing, and the latest crawl. Answers 'is this
        site set up and verified'."""
        return self.call("get_site_status", _present({"clientId": client_id}))

    def get_subdomain_traffic(self, *, client_id: str, domain: str, max_cost_micros: Optional[int] = None) -> Any:
        """See which subdomains carry a site's search traffic. A site's subdomains ranked
        by estimated organic traffic and ranking keywords, up to 50. Answers 'which
        parts of this site carry its search presence'. get_domain_facts lists subdomain
        names from certificate logs for free but says nothing of their traffic. A paid
        lookup on the client's account: quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_subdomain_traffic", _present({"clientId": client_id, "domain": domain, "maxCostMicros": max_cost_micros}))

    def get_top_searches(self, *, market: str, since: str, limit: Optional[int] = None) -> Any:
        """The terms the panel searched most. What a market actually searched for over a
        period, most-searched first, counted by distinct people rather than by events.
        Answers 'what is being looked for right now' for keyword discovery, without a
        vendor's list in between. Terms below the reporting floor never appear."""
        return self.call("get_top_searches", _present({"market": market, "since": since, "limit": limit}))

    def get_url_swaps(self, *, client_id: str, tracker_id: str, days: Optional[int] = None, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get ranking URL swaps. Tracked keywords whose ranking page changed over a period
        — which page replaced which, when, and at what positions — flagging pages that
        take turns, and any keyword where several of the client's pages rank at once
        right now. Answers 'which keywords have two of our pages fighting over them'.
        Use it alongside get_cannibalization, which looks at one snapshot rather than
        across time."""
        return self.call("get_url_swaps", _present({"clientId": client_id, "trackerId": tracker_id, "days": days, "device": device}))

    def get_vendor_connections(self) -> Any:
        """Which vendor accounts are connected. Which data vendors and AI assistants the
        agency has connected its own account for, and whether each last checked out.
        Answers 'why is this data missing' when a vendor was never connected. Never
        returns any part of a credential."""
        return self.call("get_vendor_connections", {})

    def get_web_analytics_breakdown(self, *, client_id: str, breakdown: Literal["pages", "entry_pages", "exit_pages", "sources", "referrers", "campaigns", "countries", "devices", "browsers", "os", "events"], days: Optional[float] = None, limit: Optional[int] = None) -> Any:
        """Traffic by page, source, campaign, country or device (first-party). Lists the
        top rows of one breakdown from Seolyticize's own web analytics: pages
        (pageviews), entry_pages and exit_pages (visits), sources and referrers (visits;
        key null means direct), campaigns (visits, with detail "source / medium"),
        countries (ISO codes; null means unknown), devices, browsers, os, or custom
        events (event count). Each row has key, visitors and count; counts says what
        count counts, and totalKeys how many rows exist before the limit. Answers 'which
        pages and sources drive visits'. Refuses with a sentence when web analytics has
        not been set up for the client. Free."""
        return self.call("get_web_analytics_breakdown", _present({"clientId": client_id, "breakdown": breakdown, "days": days, "limit": limit}))

    def get_web_analytics_setup(self, *, client_id: str) -> Any:
        """Is web analytics installed. Whether Seolyticize's own cookieless web analytics
        is set up for a client, with the one-line tracking snippet to install, the
        hostnames allowed to report, and lastEventAt (null until the first visit is
        recorded). Answers 'is the tracking script installed' and 'what snippet do I add
        to the site'. configured is false when no snippet has been created yet. Free."""
        return self.call("get_web_analytics_setup", _present({"clientId": client_id}))

    def get_web_analytics_summary(self, *, client_id: str, days: Optional[float] = None) -> Any:
        """Site traffic summary (first-party). Visitors, visits, pageviews, views per
        visit, bounce rate and average visit duration from Seolyticize's own web
        analytics, against the same span before (previous is null when that span was not
        fully measured), plus a daily series, realtimeVisitors in the last 30 minutes,
        and notes on how figures are counted. Answers 'how much traffic did the site
        get' for a client without GA4. Visitors are counted per day without cookies; a
        figure of null means not measured, not zero. Refuses with a sentence when web
        analytics has not been set up for the client. Free."""
        return self.call("get_web_analytics_summary", _present({"clientId": client_id, "days": days}))

    def get_written_report(self, *, client_id: str, report_id: str) -> Any:
        """Read a written report. Reads one written report: its Markdown, the rendered
        HTML, its summary, who wrote it, and its public shareUrl (null while private).
        Answers 'show me that report'. Free."""
        return self.call("get_written_report", _present({"clientId": client_id, "reportId": report_id}))

    def get_yandex_performance(self, *, client_id: str, from_: str, to: str) -> Any:
        """What Yandex Webmaster reports. The client's site as Yandex Webmaster reports it:
        site quality index, searchable and excluded pages, problems by severity, popular
        search queries with impressions, clicks and position, indexing history by HTTP
        status, sitemaps, and the recrawl queue with its quota. Answers 'how is this
        site doing in Yandex'. configured is false when this deployment has no Yandex
        app, and connected is false until the client's site owner has granted access."""
        return self.call("get_yandex_performance", _present({"clientId": client_id, "from": from_, "to": to}))

    def inspect_url(self, *, client_id: str, url: str) -> Any:
        """Ask Google what it holds for one page. Runs Google's URL Inspection on one
        address of the client's own site: whether it is indexed, Google's coverage
        state, when it was last crawled, Google's chosen canonical against the site's
        own, mobile usability (deprecated by Google and often absent) and rich results
        detected. Answers 'is this page in Google, and if not why'. Spends one of the
        property's 2,000 daily inspections; refuses addresses that are not on a site the
        agency manages for this client, and says so when the day's allowance is used."""
        return self.call("inspect_url", _present({"clientId": client_id, "url": url}))

    def issue_indexnow_key(self, *, client_id: str) -> Any:
        """Issue an IndexNow key. Issues the client's IndexNow key and returns the file to
        put on the site: fileName at the site's root, containing exactly the key.
        Answers 'set up IndexNow'. Re-issuing replaces the key and invalidates the file
        already on the site, so only do it when asked to or when the key must be
        retired. Hand the file to whoever can publish to the site (sites running the
        Seolyticize WordPress plugin serve it themselves), then call
        verify_indexnow_key."""
        return self.call("issue_indexnow_key", _present({"clientId": client_id}))

    def issue_site_verification(self, *, client_id: str, method: Optional[Literal["file", "meta", "dns"]] = None, site_url: Optional[str] = None) -> Any:
        """Issue a Google site verification. Answers 'prove we own the site to Google
        without anyone opening Search Console'. Asks Google for a verification token for
        the agency's own Google account and returns what to deploy: a file at the site
        root (file), a <head> tag (meta) or a TXT record (dns). Then call
        verify_site_ownership. onboard_site does this for you. Free."""
        return self.call("issue_site_verification", _present({"clientId": client_id, "method": method, "siteUrl": site_url}))

    def keyword_explorer(self, *, client_id: str, seed: str, mode: Optional[Literal["ideas", "suggestions", "related", "questions"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, filters: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, page: Optional[int] = None, page_size: Optional[int] = None, format_: Optional[Literal["rows", "csv"]] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Explore keyword ideas with filters. Expands a seed term into keyword ideas,
        suggestions, related terms or questions, then filters, sorts and pages them:
        include and exclude words, volume, difficulty, cost per click and word-count
        ranges, questions only, search intent, and result-page features. Answers 'which
        terms around this topic are worth going after'. The expansion is bought once per
        seed, mode and market; every later filter on the same seed is free. Rows a
        filter cannot judge because the number is unknown are left out and counted in
        unknownExcluded rather than treated as zero. Set format to csv for every
        matching row as a CSV file. Can spend: pass max_cost_micros to cap it."""
        return self.call("keyword_explorer", _present({"clientId": client_id, "seed": seed, "mode": mode, "locationCode": location_code, "languageCode": language_code, "filters": filters, "sort": sort, "page": page, "pageSize": page_size, "format": format_, "maxCostMicros": max_cost_micros}))

    def keyword_traffic_potential(self, *, client_id: str, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, refresh: Optional[bool] = None, max_cost_micros: Optional[int] = None) -> Any:
        """What ranking first for a keyword is worth. Traffic potential and parent topic
        for a keyword: the estimated monthly organic traffic of the page ranking first,
        summed across every keyword that page ranks for, and that page's highest-volume
        keyword. Answers 'how much traffic is this keyword really worth' and 'what topic
        should the page be about' — a keyword's own volume undersells it. Estimated
        through the measured click curve and labelled with its source. Null when the
        leader's rankings are unknown, never zero. May buy the results page and the
        leader's ranked keywords when the archive holds neither. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("keyword_traffic_potential", _present({"clientId": client_id, "term": term, "locationCode": location_code, "languageCode": language_code, "refresh": refresh, "maxCostMicros": max_cost_micros}))

    def list_alert_rules(self, *, client_id: str) -> Any:
        """List alert rules. What a client's alerts watch for, at what threshold, and
        whether each is paused. Lists the rules; list_recent_alerts lists what they
        fired."""
        return self.call("list_alert_rules", _present({"clientId": client_id}))

    def list_api_activity(self, *, since_hours: Optional[int] = None, key_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """List API activity. Recent tool calls made with the agency's keys — which key,
        which tool, which client, how it ended and how long it took — newest first.
        Lists who did what through the API and MCP. Inputs are never recorded."""
        return self.call("list_api_activity", _present({"sinceHours": since_hours, "keyId": key_id, "limit": limit}))

    def list_api_keys(self) -> Any:
        """List API keys. The agency's live API keys with name, role, which client each is
        pinned to and when it was last used. Lists keys to audit or revoke. Never
        returns a key."""
        return self.call("list_api_keys", {})

    def list_clients(self) -> Any:
        """List clients. Lists every client the caller can access. Use this first when a
        request names a client by name rather than id."""
        return self.call("list_clients", {})

    def list_connected_apps(self) -> Any:
        """List connected apps. Assistants and agent apps connected to the agency by
        signing in (MCP OAuth) rather than with an API key: which app, the role and
        client it was given, who approved it, and when it was last used. Answers 'what
        has access to our account'."""
        return self.call("list_connected_apps", {})

    def list_crawl_issues(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """List site audit issues. Technical issues one crawl found, by rule: its readable
        label, severity, category, how many pages it affects, and howToFix — concrete
        steps to fix it and check the fix. Lists what to fix. Use crawlId 'latest' for
        the newest completed crawl."""
        return self.call("list_crawl_issues", _present({"clientId": client_id, "crawlId": crawl_id}))

    def list_crawls(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """List crawls. A client's recent crawls of every status, newest first. Lists what
        the crawler has been doing, including crawls that failed."""
        return self.call("list_crawls", _present({"clientId": client_id, "limit": limit}))

    def list_invite_codes(self) -> Any:
        """List invite codes. Lists the agency's invite codes — label, uses left, expiry,
        whether revoked — never the codes themselves. Answers 'which invite codes are
        out there'. Free."""
        return self.call("list_invite_codes", {})

    def list_issue_pages(self, *, client_id: str, rule_id: str, crawl_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
        """List the pages an issue is on. Lists the pages where one crawl issue was found,
        with the message for each page, so they can be fixed. Answers 'which pages have
        missing titles' or 'where are the broken links'. ruleId comes from
        get_audit_summary or list_crawl_issues; crawlId defaults to the latest completed
        crawl. Paged: limit (up to 500) and offset; total is the whole count. Free."""
        return self.call("list_issue_pages", _present({"clientId": client_id, "ruleId": rule_id, "crawlId": crawl_id, "limit": limit, "offset": offset}))

    def list_keyword_lists(self, *, client_id: Optional[str] = None) -> Any:
        """List keyword lists. The keyword lists the caller can see, with how many keywords
        each holds — one client's, or every list the caller may reach when no client is
        named. Answers 'where did we save those keywords'. The agency's own lists, which
        belong to no client, are only visible to people who can see every client."""
        return self.call("list_keyword_lists", _present({"clientId": client_id}))

    def list_link_prospects(self, *, client_id: str) -> Any:
        """List a client's link prospects. The client's outreach list: sites worth asking
        for a link, each with its stage (identified, contacted, replied, won, rejected),
        why it was added, and when it last moved, most recently moved first. Answers
        'where is our link outreach'. Free."""
        return self.call("list_link_prospects", _present({"clientId": client_id}))

    def list_local_locations(self, *, client_id: str) -> Any:
        """List a client's business locations. The client's business locations for local
        SEO: id, name, latitude and longitude. Answers 'which locations do we track in
        the map pack'. Pass an id to get_local_visibility, run_local_grid_scan or
        sync_local_reviews. Free."""
        return self.call("list_local_locations", _present({"clientId": client_id}))

    def list_markets(self, *, query: Optional[str] = None) -> Any:
        """Find a market's location code. Lists the countries and regions this product
        measures, with the location code other tools take (locationCode), the ISO code
        and Google's own country code. Search by name, ISO code (gb), Google code (uk)
        or location code (2826); an exact code wins over a name match. Answers 'what is
        the location code for Germany'. Only markets the product can measure honestly
        are listed. Free."""
        return self.call("list_markets", _present({"query": query}))

    def list_portal_links(self, *, client_id: str) -> Any:
        """List client portal links. The live white-label portal links for a client: label,
        when each was made, and when it was last opened. Lists who can currently see the
        client's results without an account. The addresses themselves are not shown —
        they exist only at the moment a link is made."""
        return self.call("list_portal_links", _present({"clientId": client_id}))

    def list_projects(self, *, client_id: str) -> Any:
        """List projects and sites. A client's projects with the sites under each. Lists
        where crawls and trackers hang from."""
        return self.call("list_projects", _present({"clientId": client_id}))

    def list_rank_trackers(self, *, client_id: str) -> Any:
        """List rank trackers. A client's rank trackers with engine, device, cadence and
        locale. Lists the tracker ids the ranking tools take."""
        return self.call("list_rank_trackers", _present({"clientId": client_id}))

    def list_recent_alerts(self, *, client_id: str, since: str) -> Any:
        """List recent alerts. Alerts raised for a client since a given time, newest first.
        Lists what has fired, for anything watching — a chat channel, an automation, a
        status board."""
        return self.call("list_recent_alerts", _present({"clientId": client_id, "since": since}))

    def list_report_schedules(self, *, client_id: str) -> Any:
        """List report schedules. Every schedule that emails one of a client's saved
        reports: which report, monthly or weekly, the recipients, whether it is paused
        and when it last sent. Lists who receives what and how often. send_report sends
        to these recipients, so a report with no schedule has nobody to send to."""
        return self.call("list_report_schedules", _present({"clientId": client_id}))

    def list_report_templates(self, *, client_id: Optional[str] = None) -> Any:
        """List report templates. Lists the report templates that apply: the agency's own,
        plus the client's when clientId is given — each with its audience, sections in
        order with guidance, tone and sign-off. Answers 'how do we usually write this
        report'. Follow a template's sections and tone when writing a report it fits,
        and name it in save_written_report. Free."""
        return self.call("list_report_templates", _present({"clientId": client_id}))

    def list_reports(self, *, client_id: str) -> Any:
        """List reports. A client's saved reports and their recent deliveries, including
        failed ones with the reason. Lists what goes out and answers 'did my report go
        out'."""
        return self.call("list_reports", _present({"clientId": client_id}))

    def list_sitemaps(self, *, client_id: str) -> Any:
        """The sitemaps each search engine knows about. The client's sitemaps as Google,
        Bing and Yandex each report them: submitted URL counts, errors and warnings,
        when each was last read. Answers 'are our sitemaps being read, and are they
        broken'. Google no longer reports how many of a sitemap's URLs are indexed, so
        that figure is always null; instead, of the pages inspected, how many came from
        each sitemap and passed. Each engine's part is separately present, refused or
        failed."""
        return self.call("list_sitemaps", _present({"clientId": client_id}))

    def list_team_members(self) -> Any:
        """List the team. Everyone with access to the agency: email, name, role, and the
        clients each is limited to (empty means agency-wide). Also lists the clients a
        new member could be limited to. Answers 'who can see this account'."""
        return self.call("list_team_members", {})

    def list_tracked_keywords(self, *, client_id: str, tracker_id: str) -> Any:
        """List tracked keywords. The terms a tracker measures and the competitor domains
        it compares against. Lists what is being paid for on every run."""
        return self.call("list_tracked_keywords", _present({"clientId": client_id, "trackerId": tracker_id}))

    def list_written_reports(self, *, client_id: str) -> Any:
        """List written reports. Lists the written reports saved for a client, newest
        change first: id, title, a plain-text summary, who wrote and last changed it,
        and whether it is shared. Answers 'what reports have we written for this
        client'. Call it before save_written_report to find a report to replace rather
        than writing a duplicate. Free."""
        return self.call("list_written_reports", _present({"clientId": client_id}))

    def onboard_site(self, *, domain: str, name: Optional[str] = None, framework: Optional[Literal["nextjs", "astro", "remix", "sveltekit", "nuxt", "html", "wordpress", "other"]] = None, keywords: Optional[List[str]] = None, verification: Optional[Literal["file", "meta", "dns"]] = None) -> Any:
        """Onboard a site in one call. Answers 'set this site up'. Makes the client,
        project, site and rank tracker — or finds the client already here for this
        domain, so calling it twice is safe — issues the IndexNow key and a Google site
        verification for the agency's own Google account, sets up cookieless analytics,
        and returns one deploy manifest: files to serve at exact paths, tags for the
        <head>, the analytics snippet placed for the framework given, and CSP entries.
        Deploy all of it, then call verify_site. No Google sign-in or Search Console
        settings are needed at any point. Free."""
        return self.call("onboard_site", _present({"domain": domain, "name": name, "framework": framework, "keywords": keywords, "verification": verification}))

    def page_headers(self, *, url: str, max_cost_micros: Optional[int] = None) -> Any:
        """What the server actually returned. Status code, redirect chain, content type and
        the headers that decide indexing for one address. Answers 'why is this page not
        in the index' when the markup looks fine — an X-Robots-Tag noindex is invisible
        to anything reading the page. Can spend: pass max_cost_micros to cap it."""
        return self.call("page_headers", _present({"url": url, "maxCostMicros": max_cost_micros}))

    def page_lab(self, *, url: str, strategy: Optional[Literal["mobile", "desktop"]] = None, max_cost_micros: Optional[int] = None) -> Any:
        """How a page scores in one synthetic run. Lighthouse performance, SEO,
        accessibility and best-practices scores for one address, from PageSpeed
        Insights. Answers 'what is slow or wrong on this page' with a reproducible lab
        run, including for pages too quiet for field data. This is not what real
        visitors experienced — use page_vitals for that, and say which is which when
        reporting both. There is no interaction metric here: a synthetic run interacts
        with nothing. Can spend: pass max_cost_micros to cap it."""
        return self.call("page_lab", _present({"url": url, "strategy": strategy, "maxCostMicros": max_cost_micros}))

    def page_vitals(self, *, url: str) -> Any:
        """How a page performs for real visitors. Largest Contentful Paint, Interaction to
        Next Paint and Cumulative Layout Shift for one address, from the Chrome UX
        Report. Answers 'is this page fast enough for real visitors' with field data
        over a trailing 28 days, which is what Google ranks on rather than a lab score."""
        return self.call("page_vitals", _present({"url": url}))

    def pin_tracked_keywords(self, *, client_id: str, tracker_id: str, keyword_ids: List[str], pinned: Optional[bool] = None) -> Any:
        """Pin tracked keywords to the top. Pins tracked keywords (by keywordId from
        list_tracked_keywords or get_rank_history) to the top of a tracker's table for
        everyone on the account, or unpins them with pinned false. Pinned keywords are
        listed first, in the order they were pinned. Ids not on the tracker are ignored;
        changed says how many moved. Answers 'keep these at the top'. Free."""
        return self.call("pin_tracked_keywords", _present({"clientId": client_id, "trackerId": tracker_id, "keywordIds": keyword_ids, "pinned": pinned}))

    def queue_url_inspections(self, *, client_id: str, urls: List[str]) -> Any:
        """Queue URLs for Search Console inspection. Queues up to 500 of the client's URLs
        for Search Console's URL inspection, which runs in the background within
        Google's daily allowance. Answers 'check whether all these pages are indexed'.
        URLs that are not on the client's own site are refused and listed with the
        reason. Read the results with get_index_coverage as they arrive; inspect_url
        checks one URL immediately. Needs Search Console connected (see
        get_connection_link)."""
        return self.call("queue_url_inspections", _present({"clientId": client_id, "urls": urls}))

    def recheck_links(self, *, client_id: str) -> Any:
        """Re-check the pages that link to a client. Sends our crawler to the pages said to
        link to the client to see whether each still does — slowly and politely, so it
        takes a while; read the result with get_link_checks. A second request within the
        hour lands on the check already running. No vendor charge, but it visits other
        people's sites on the client's behalf, so it needs client:manage. Refused when
        the client has no rank tracker yet. Answers 'check our links again'."""
        return self.call("recheck_links", _present({"clientId": client_id}))

    def refresh_domain_data(self, *, client_id: str, max_cost_micros: Optional[int] = None) -> Any:
        """Refresh domain and backlink data now. Refreshes everything bought about the
        client's domain — overview, ranked keywords, competitors, top pages and the
        backlink profile — plus what up to five tracked competitors rank for and who
        links to them. Answers 'update the backlinks and keyword data'. The dearest
        thing the product does: quote it with estimate_cost first; with maxCostMicros
        the refresh is refused before it starts when its estimate is over the limit.
        Runs in the background for a few minutes: poll get_run_status with job 'domain'.
        A second request within the hour lands on the refresh already going. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("refresh_domain_data", _present({"clientId": client_id, "maxCostMicros": max_cost_micros}))

    def refresh_rankings(self, *, client_id: str, max_cost_micros: Optional[int] = None) -> Any:
        """Capture rankings now. Captures the client's rank tracker now instead of at its
        next scheduled run: every tracked keyword on every device the tracker reads,
        each a paid lookup. Answers 'get me today's positions'. Quote it with
        estimate_cost first; with maxCostMicros the run is refused before it starts when
        its estimate is over the limit. Runs in the background: poll get_run_status with
        job 'rank', then read get_rankings or get_rank_summary. A second request within
        the same minute lands on the run already going rather than paying twice. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("refresh_rankings", _present({"clientId": client_id, "maxCostMicros": max_cost_micros}))

    def remove_competitors(self, *, client_id: str, tracker_id: str, domains: List[str]) -> Any:
        """Remove competitors from a tracker. Stops measuring the named competitor domains
        on a rank tracker. Answers 'we no longer compete with this site'. Returns the
        tracker's remaining competitors. Naming a domain that is not on the list is not
        an error."""
        return self.call("remove_competitors", _present({"clientId": client_id, "trackerId": tracker_id, "domains": domains}))

    def remove_keywords_from_list(self, *, list_id: str, keyword_ids: List[str]) -> Any:
        """Remove keywords from a list. Removes keywords from a list by keyword id. Tracked
        keywords that came from the list stay tracked. Answers 'take these off that
        list'."""
        return self.call("remove_keywords_from_list", _present({"listId": list_id, "keywordIds": keyword_ids}))

    def remove_team_member(self, *, membership_id: str) -> Any:
        """Remove someone from the team. Ends a member's access to the agency, by the
        membershipId list_team_members gives. Answers 'Sam has left'. Their account
        itself is untouched. The last owner cannot be removed. Safe to repeat."""
        return self.call("remove_team_member", _present({"membershipId": membership_id}))

    def remove_tracked_keywords(self, *, client_id: str, tracker_id: str, terms: List[str]) -> Any:
        """Stop tracking keywords. Removes terms from a tracker. Answers 'stop tracking
        these keywords'. Terms that were not tracked are ignored, so it is safe to
        repeat."""
        return self.call("remove_tracked_keywords", _present({"clientId": client_id, "trackerId": tracker_id, "terms": terms}))

    def remove_vendor_credential(self, *, provider: Literal["dataforseo", "serpapi", "anthropic", "bingwebmaster", "reportwebhook", "serpproxy", "googleads", "crux", "chatgpt", "gemini", "perplexity", "grok", "meta-ai", "deepseek", "pagespeed", "telegram"]) -> Any:
        """Disconnect a vendor account. Deletes the agency's saved account for one vendor.
        Answers 'stop using our DataForSEO account'. Anything that relied on it —
        keyword data from DataForSEO, an assistant's answers — stops until another is
        saved. Safe to repeat."""
        return self.call("remove_vendor_credential", _present({"provider": provider}))

    def rename_keyword_list(self, *, list_id: str, name: str) -> Any:
        """Rename a keyword list. Gives a keyword list a new name. Answers 'call that list
        something else'. Refused when another list for the same client (or the agency)
        already has the name."""
        return self.call("rename_keyword_list", _present({"listId": list_id, "name": name}))

    def revoke_api_key(self, *, key_id: str) -> Any:
        """Revoke an API key. Stops a key working, immediately and for good. Answers 'this
        key leaked'. Safe to repeat; revoking the key making the call is allowed and
        takes effect on its next request."""
        return self.call("revoke_api_key", _present({"keyId": key_id}))

    def revoke_deploy_hook(self, *, client_id: str) -> Any:
        """Revoke the deploy hook. Answers 'that deploy hook URL leaked'. Stops the
        client's deploy hook URL working at once. Free."""
        return self.call("revoke_deploy_hook", _present({"clientId": client_id}))

    def revoke_invite_code(self, *, invite_code_id: str) -> Any:
        """Revoke an invite code. Stops an invite code being claimed again. Answers 'that
        code was shared too widely'. Keys already made from it keep working until
        revoked with revoke_api_key. Free."""
        return self.call("revoke_invite_code", _present({"inviteCodeId": invite_code_id}))

    def revoke_portal_link(self, *, client_id: str, link_id: str) -> Any:
        """Revoke a client portal link. Stops a portal link working, immediately and for
        good. Answers 'that link was forwarded' or 'the engagement ended'. A link that
        is already revoked, or is not this client's, is refused rather than reported as
        done."""
        return self.call("revoke_portal_link", _present({"clientId": client_id, "linkId": link_id}))

    def run_ai_visibility_check(self, *, client_id: str, max_cost_micros: Optional[int] = None) -> Any:
        """Run an AI visibility check now. Asks every tracked question on the chosen
        assistants now, in the background; results arrive within minutes in
        get_ai_visibility_runs and get_ai_visibility_results. The schedule is unchanged.
        With maxCostMicros, the check is refused before it starts when its estimate is
        over the limit. Get the user's go-ahead first: it spends. Answers 'check it
        now'. Can spend: pass max_cost_micros to cap it."""
        return self.call("run_ai_visibility_check", _present({"clientId": client_id, "maxCostMicros": max_cost_micros}))

    def run_local_grid_scan(self, *, client_id: str, location_id: str, term: str, size: Optional[float] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Run a map-pack grid scan. Searches the term at every point of a size × size grid
        around the location (1.5 km apart) and records where the business appears in the
        map pack. Every point is a paid lookup, so a 7 × 7 grid is 49 lookups: quote it
        with estimate_cost and get the user's go-ahead first. Runs in the background;
        read the result with get_local_visibility a few minutes later. With
        maxCostMicros, the scan is refused before it starts when its estimate is over
        the limit. Answers 'scan our map-pack visibility now'. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("run_local_grid_scan", _present({"clientId": client_id, "locationId": location_id, "term": term, "size": size, "maxCostMicros": max_cost_micros}))

    def save_ai_visibility_setup(self, *, client_id: str, add_prompts: Optional[List[Dict[str, Any]]] = None, retire_prompt_ids: Optional[List[str]] = None, add_brands: Optional[List[Dict[str, Any]]] = None) -> Any:
        """Change what AI visibility tracks. Adds questions (each optionally with a
        two-letter market), retires questions by id (past answers keep their question),
        and adds brands to look for (name, domain, aliases; isClient for the client's
        own — there should be exactly one). Questions already tracked are skipped. Write
        questions the way a buyer would ask an assistant, without naming any brand;
        suggest_ai_prompts drafts them. Answers 'track these questions'. Free; the
        checks that follow are what cost."""
        return self.call("save_ai_visibility_setup", _present({"clientId": client_id, "addPrompts": add_prompts, "retirePromptIds": retire_prompt_ids, "addBrands": add_brands}))

    def save_baidu_token(self, *, client_id: str, site_url: str, token: str) -> Any:
        """Save the client's Baidu push token. Saves the link-push token from Baidu Ziyuan
        (ziyuan.baidu.com, link submission page) for the client's site, so
        submit_baidu_urls can push pages. Answers 'connect Baidu for this client'. The
        site must be the client's own registered site; the token is stored encrypted and
        never returned. Replaces any token already saved."""
        return self.call("save_baidu_token", _present({"clientId": client_id, "siteUrl": site_url, "token": token}))

    def save_report_template(self, *, name: str, sections: List[Dict[str, Any]], template_id: Optional[str] = None, client_id: Optional[str] = None, description: Optional[str] = None, audience: Optional[str] = None, tone: Optional[str] = None, sign_off: Optional[str] = None) -> Any:
        """Save a report template. Saves a reusable brief for a kind of report: a name, who
        it is for, sections in order (each with a line on what goes under it), tone and
        sign-off. Answers 'make this our monthly report format'. Without clientId it is
        agency-wide, which only someone who sees every client may change; with one it is
        that client's own. Without templateId a new template is made; with one, it is
        replaced. Only save a template when the user asks for one — a one-off report
        needs none. Free."""
        return self.call("save_report_template", _present({"templateId": template_id, "clientId": client_id, "name": name, "description": description, "audience": audience, "sections": sections, "tone": tone, "signOff": sign_off}))

    def save_vendor_credential(self, *, provider: Literal["dataforseo", "serpapi", "anthropic", "bingwebmaster", "reportwebhook", "serpproxy", "googleads", "crux", "chatgpt", "gemini", "perplexity", "grok", "meta-ai", "deepseek", "pagespeed", "telegram"], secret: str, login: Optional[str] = None, google_ads: Optional[Dict[str, Any]] = None) -> Any:
        """Connect a vendor account. Stores the agency's own account for a data vendor or
        AI assistant — DataForSEO (login + password), SerpApi, a proxy pool (serpproxy:
        one URL per line), Google Ads (six values in googleAds), an Anthropic, OpenAI,
        Gemini or Perplexity key, and the rest get_vendor_connections names — and checks
        it works straight away. Answers 'connect our DataForSEO account'. Replaces any
        key already saved for that vendor. The response says whether the check passed;
        it never contains the key."""
        return self.call("save_vendor_credential", _present({"provider": provider, "login": login, "secret": secret, "googleAds": google_ads}))

    def save_written_report(self, *, client_id: str, title: str, markdown: str, report_id: Optional[str] = None, template_id: Optional[str] = None) -> Any:
        """Save a written report. Saves a finished report to a client, where everyone on
        the account can read and print it. Answers 'save this report for the client'.
        Write it in Markdown (headings, lists, tables, links); raw HTML is shown as
        text, not run. Without reportId a new report is created; with one, that report's
        title and text are replaced and its share link, if any, keeps working. Name
        templateId when it was written to a report template. New reports are private —
        use set_report_sharing only when the user asks for a link. Free."""
        return self.call("save_written_report", _present({"clientId": client_id, "reportId": report_id, "title": title, "markdown": markdown, "templateId": template_id}))

    def schedule_report(self, *, client_id: str, report_id: str, recipients: List[str], cadence: Optional[Literal["monthly", "weekly"]] = None) -> Any:
        """Schedule a report. Puts one of a client's saved reports (see list_reports,
        create_report) on a monthly or weekly cadence for a list of recipients. Answers
        'send this report to the client every month'. The scheduled send runs on its
        own; send_report sends one now, to every recipient of every schedule for that
        report. A report can have more than one schedule."""
        return self.call("schedule_report", _present({"clientId": client_id, "reportId": report_id, "cadence": cadence, "recipients": recipients}))

    def send_report(self, *, client_id: str, report_id: str, idempotency_key: Optional[str] = None) -> Any:
        """Send a report now. Sends a saved report to its scheduled recipients now,
        covering the month just gone. Answers 'send the report'. Recipients come from
        the report's schedule and cannot be named here. Pass an idempotencyKey to make a
        retry land on the same send instead of emailing the client twice."""
        return self.call("send_report", _present({"clientId": client_id, "reportId": report_id, "idempotencyKey": idempotency_key}))

    def serp_overview(self, *, client_id: str, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, refresh: Optional[bool] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Who is on the first page for a keyword. The current top ten organic results for
        a keyword, each with domain authority, referring domains, the estimated organic
        traffic of that page, links into the page where counted, and every feature on
        the results page — plus why the keyword's difficulty is what it is. Answers
        'could we get onto that page, and who would we have to beat'. Read from a recent
        capture when one is held, bought otherwise. Each figure says where it came from
        (our link graph or the vendor; panel or published click curve), and anything
        unknown is null, never zero. Can spend: pass max_cost_micros to cap it."""
        return self.call("serp_overview", _present({"clientId": client_id, "term": term, "locationCode": location_code, "languageCode": language_code, "refresh": refresh, "maxCostMicros": max_cost_micros}))

    def set_ai_visibility_schedule(self, *, client_id: str, cadence: Optional[Literal["off", "daily", "weekly", "monthly"]] = None, engines: Optional[List[Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"]]] = None) -> Any:
        """Set how often AI visibility is checked. Sets a client's cadence (off, daily,
        weekly or monthly; weekly unless changed) and which assistants it is checked on
        (engines; null or empty for every one the agency has configured). Every
        scheduled check asks every question on every chosen assistant, so show
        estimate_ai_visibility_cost first. Answers 'check this daily on ChatGPT and
        Perplexity'. Free to set."""
        return self.call("set_ai_visibility_schedule", _present({"clientId": client_id, "cadence": cadence, "engines": engines}))

    def set_branding(self, *, name: str, logo_url: str, primary_color: str) -> Any:
        """Set the agency's branding. Renames the agency and sets the logo and colour on
        its reports and portal links. Answers 'put our logo on the reports'. The logo
        must be an https:// address and the colour six-digit hex such as #1f5ad6; empty
        strings clear them. Send all three: this replaces what is there."""
        return self.call("set_branding", _present({"name": name, "logoUrl": logo_url, "primaryColor": primary_color}))

    def set_keyword_notes(self, *, list_id: str, notes: List[Dict[str, Any]]) -> Any:
        """Note why keywords are on a list. Sets notes on keywords in a list — why each is
        there, which page it belongs to, what was decided — by keywordId from
        get_keyword_list. An empty note clears it; ids not on the list are ignored and
        changed says how many were set. Answers 'note that this one is for the implants
        page'. Free."""
        return self.call("set_keyword_notes", _present({"listId": list_id, "notes": notes}))

    def set_link_prospect_status(self, *, client_id: str, prospect_id: str, status: Literal["identified", "contacted", "replied", "won", "rejected"]) -> Any:
        """Move a link prospect to another stage. Moves one prospect on the client's
        outreach list to identified, contacted, replied, won or rejected. Take the id
        from list_link_prospects. Answers 'we heard back from this site'. Free."""
        return self.call("set_link_prospect_status", _present({"clientId": client_id, "prospectId": prospect_id, "status": status}))

    def set_report_sharing(self, *, client_id: str, report_id: str, shared: bool) -> Any:
        """Share a written report by link. Turns a written report's public link on or off.
        Answers 'give me a link I can send the client'. Anyone holding the link can read
        the report without an account, so only turn it on when the user explicitly asks.
        Turning it on for a report already shared returns the same link; turning it off
        breaks the link immediately, and sharing again later makes a new one. The page
        carries a preview card for Slack, email and social networks. Free."""
        return self.call("set_report_sharing", _present({"clientId": client_id, "reportId": report_id, "shared": shared}))

    def set_up_web_analytics(self, *, client_id: str, hostnames: Optional[List[str]] = None, exclude_paths: Optional[List[str]] = None, include_paths: Optional[List[str]] = None) -> Any:
        """Set up web analytics. Creates a client's cookieless web analytics, or changes
        which hostnames may report to it, and returns the same shape as
        get_web_analytics_setup: the one-line tracking snippet to add to every page, the
        allowed hostnames and lastEventAt. Answers 'install tracking on this site'.
        Without hostnames it allows the client's own domain and its www form; with
        hostnames, those replace the list (up to 20; a visit from any other hostname is
        ignored, so add staging or extra domains here). Safe to repeat: an existing
        setup keeps its snippet. configured is false when the client has no site domain
        to default to and no hostnames were given. Free."""
        return self.call("set_up_web_analytics", _present({"clientId": client_id, "hostnames": hostnames, "excludePaths": exclude_paths, "includePaths": include_paths}))

    def start_crawl(self, *, client_id: str) -> Any:
        """Start a site audit crawl. Crawls the client's site now rather than waiting for
        the schedule. Answers 'audit the site again'. If a crawl is already running it
        is returned instead of starting a second. Poll get_crawl_status with the crawl
        id; read results with list_crawl_issues."""
        return self.call("start_crawl", _present({"clientId": client_id}))

    def striking_distance(self, *, client_id: str, days: Optional[int] = None, min_position: Optional[float] = None, max_position: Optional[float] = None, min_impressions: Optional[int] = None) -> Any:
        """Queries just off the top, by page. Search Console queries where the client
        already ranks around positions four to twenty with meaningful impressions,
        grouped by the page that ranks. Each has the expected click-through rate now and
        at the top three from the measured click curve, the extra monthly clicks a move
        to third (and to first) would bring, and an opportunity score that favours
        queries nearest the top. Answers 'which existing pages should we improve first'.
        Read from stored console data; buys nothing. Null when the client has no site
        configured."""
        return self.call("striking_distance", _present({"clientId": client_id, "days": days, "minPosition": min_position, "maxPosition": max_position, "minImpressions": min_impressions}))

    def submit_baidu_urls(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Push pages to Baidu. Pushes addresses on the client's own site to Baidu through
        Ziyuan's link submission, the only API Baidu offers a site owner. Answers 'tell
        Baidu about these pages'. Returns how many Baidu accepted and how many more it
        will take today — Baidu reports its allowance only in reply to a push. Refuses
        addresses not on the client's registered site, and refuses entirely when no
        Baidu token has been saved. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_baidu_urls", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros}))

    def submit_indexnow(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Tell search engines a page changed. Submits changed addresses to IndexNow, which
        Bing, Yandex, Seznam and Naver share. Google does not take part. Only accepts
        addresses on a site the agency manages — anything else is refused and named.
        Answers 'we have just republished these pages, tell the engines'. Refuses
        entirely until the client's key file has been published and checked. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("submit_indexnow", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros}))

    def submit_sitemap(self, *, client_id: str, sitemap_url: str) -> Any:
        """Submit a sitemap to Google. Submits a sitemap address to the client's Google
        Search Console property. Answers 'tell Google about this sitemap'. Refuses an
        address that is not on a site the agency manages for this client, Connected by
        the agency's Google account (verify_site, or the account added as a user), it
        submits directly — no further permission; Google itself refuses if that account
        is only a Restricted user, and the refusal says what to change. Connected by
        someone's Google sign-in, it needs sitemap management allowed separately (a
        second Google permission, never assumed from the read-only one)."""
        return self.call("submit_sitemap", _present({"clientId": client_id, "sitemapUrl": sitemap_url}))

    def submit_urls(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Submit URLs for crawling. Adds addresses to the crawl frontier for a client.
        Only accepts addresses on a site the agency manages — anything else is refused
        and named. Answers 'crawl these pages I found'. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("submit_urls", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros}))

    def submit_yandex_recrawl(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None) -> Any:
        """Ask Yandex to recrawl pages. Asks Yandex Webmaster to recrawl pages of the
        client's verified Yandex host, one task per page. Answers 'get Yandex to look at
        these pages again'. Returns the task id Yandex gave each queued page;
        get_yandex_performance shows the queue and the day's remaining quota. Refuses
        addresses not on the verified host (Yandex treats www and the bare domain as
        different hosts). The first quota refusal stops the rest, which come back as not
        sent. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_yandex_recrawl", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros}))

    def suggest_ai_prompts(self, *, client_id: str, topic: Optional[str] = None, count: Optional[int] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Suggest questions to track. Drafts questions worth tracking, grouped by topic,
        from the client brief, its brands and what is already tracked — phrased as a
        buyer would ask an assistant, never naming a tracked brand, never repeating a
        tracked question. Optionally around one topic. Nothing is saved: show them, then
        save the chosen ones with save_ai_visibility_setup. For questions people
        actually search, use keyword_explorer with mode questions. Answers 'what should
        we be tracking'. A metered Claude call. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("suggest_ai_prompts", _present({"clientId": client_id, "topic": topic, "count": count, "maxCostMicros": max_cost_micros}))

    def sync_local_reviews(self, *, client_id: str, location_id: str, max_cost_micros: Optional[int] = None) -> Any:
        """Collect a location's Google reviews. Collects the location's latest Google
        reviews (up to 50) from the vendor. Paid: quote it with estimate_cost first.
        Runs in the background and takes a few minutes; read the analysis with
        get_local_visibility afterwards. A second request within the hour lands on the
        collection already running rather than paying twice. With maxCostMicros, it is
        refused before it starts when its estimate is over the limit. Answers 'pull in
        our latest reviews'. Can spend: pass max_cost_micros to cap it."""
        return self.call("sync_local_reviews", _present({"clientId": client_id, "locationId": location_id, "maxCostMicros": max_cost_micros}))

    def tag_keywords(self, *, client_id: str, tracker_id: str, keyword_ids: List[str], tags: List[str], remove: Optional[bool] = None) -> Any:
        """Tag tracked keywords. Puts tags on a tracker's keywords, or takes them off with
        remove: true. Answers 'label these as our brand terms'. Tags are
        case-insensitive labels such as 'brand' or 'money terms' that the tracker view
        filters by. Keywords the tracker does not track are returned in notTracked
        rather than tagged."""
        return self.call("tag_keywords", _present({"clientId": client_id, "trackerId": tracker_id, "keywordIds": keyword_ids, "tags": tags, "remove": remove}))

    def update_alert_rule(self, *, client_id: str, rule_id: str, threshold: Optional[int] = None, cooldown_hours: Optional[int] = None, webhook_url: Optional[str] = None, channel: Optional[Literal["slack", "webhook", "email", "telegram"]] = None, email_recipients: Optional[List[str]] = None, telegram_chat_id: Optional[str] = None, paused: Optional[bool] = None) -> Any:
        """Update an alert rule. Changes a rule's threshold, cooldown or delivery (channel,
        webhookUrl — null removes it — emailRecipients, telegramChatId), or pauses and
        resumes it. Answers 'this alert is too noisy', 'send this to email instead' or
        'mute this for now'. Pausing keeps the rule's history."""
        return self.call("update_alert_rule", _present({"clientId": client_id, "ruleId": rule_id, "threshold": threshold, "cooldownHours": cooldown_hours, "webhookUrl": webhook_url, "channel": channel, "emailRecipients": email_recipients, "telegramChatId": telegram_chat_id, "paused": paused}))

    def update_client(self, *, client_id: str, name: Optional[str] = None, monthly_budget_usd: Optional[float] = None) -> Any:
        """Update a client. Renames a client or changes its monthly vendor spend cap (null
        removes the cap). Answers 'rename this client' or 'cap this client's spend'. The
        cap is enforced on every paid lookup from then on."""
        return self.call("update_client", _present({"clientId": client_id, "name": name, "monthlyBudgetUsd": monthly_budget_usd}))

    def update_client_brief(self, *, client_id: str, overview: Optional[str] = None, goal: Optional[str] = None, positioning: Optional[str] = None, audience: Optional[str] = None, voice: Optional[str] = None, add: Optional[List[Dict[str, Any]]] = None, update: Optional[List[Dict[str, Any]]] = None, remove: Optional[List[str]] = None) -> Any:
        """Update the client brief. Changes the client brief that every teammate and agent
        reads. Answers 'remember this about the client'. Set fields (overview, goal,
        positioning, audience, voice; null or empty clears one, fields left out are
        untouched); add entries (kind competitor, key_page, section or research, each
        with a title and optional body and url); edit entries by id; remove entries by
        id (unknown ids are ignored). Applied in that order, so removing an old
        competitor and adding its replacement in one call works. Record a research entry
        when you finish a piece of work whose conclusions the next one should start
        from; the 50 newest research notes are kept. Returns the brief as it now stands.
        Free."""
        return self.call("update_client_brief", _present({"clientId": client_id, "overview": overview, "goal": goal, "positioning": positioning, "audience": audience, "voice": voice, "add": add, "update": update, "remove": remove}))

    def update_rank_tracker(self, *, client_id: str, tracker_id: str, name: Optional[str] = None, device: Optional[Literal["desktop", "mobile", "both"]] = None, frequency: Optional[Literal["daily", "weekly"]] = None) -> Any:
        """Update a rank tracker. Renames a tracker or changes its device (desktop, mobile
        or both) or cadence (daily or weekly). Answers 'check these weekly instead'.
        Weekly costs a seventh as much."""
        return self.call("update_rank_tracker", _present({"clientId": client_id, "trackerId": tracker_id, "name": name, "device": device, "frequency": frequency}))

    def update_report_schedule(self, *, client_id: str, schedule_id: str, cadence: Optional[Literal["monthly", "weekly"]] = None, recipients: Optional[List[str]] = None, paused: Optional[bool] = None) -> Any:
        """Change a report schedule. Changes a schedule's cadence or recipients, or pauses
        or resumes it. Answers 'add the new marketing lead to the monthly report' and
        'stop the weekly email while the client is away'. Recipients, when given,
        replace the whole list. A paused schedule sends nothing until resumed."""
        return self.call("update_report_schedule", _present({"clientId": client_id, "scheduleId": schedule_id, "cadence": cadence, "recipients": recipients, "paused": paused}))

    def verify_indexnow_key(self, *, client_id: str) -> Any:
        """Verify the IndexNow key file. Fetches the key file from the client's site and
        records whether it is there and correct. Answers 'is IndexNow set up'.
        submit_indexnow submits only for a verified key. A failure says what was found
        instead (not served, wrong content, unreachable); a site that stops serving the
        file loses its verification."""
        return self.call("verify_indexnow_key", _present({"clientId": client_id}))

    def verify_site(self, *, client_id: str) -> Any:
        """Verify a deployed site and finish onboarding. Answers 'I deployed it, is
        everything connected'. After the onboard_site manifest is live, checks and
        completes everything in one call: the IndexNow key file, Google ownership (and
        then adds and connects the Search Console property, with its sixteen months of
        history), whether analytics has received its first event, that robots.txt and
        the sitemap answer, and starts the first crawl. Returns a checklist where every
        item not done carries the exact fix and the next call. Safe to call again. Free."""
        return self.call("verify_site", _present({"clientId": client_id}))

    def verify_site_ownership(self, *, client_id: str, method: Optional[Literal["file", "meta", "dns"]] = None, site_url: Optional[str] = None, add_owners: Optional[List[str]] = None) -> Any:
        """Verify site ownership and connect Search Console. Answers 'the verification file
        is live, connect Search Console'. Has Google check the deployed file, tag or
        record (with no method, each is tried), which makes the agency's Google account
        a verified owner; then adds the property to its Search Console and connects it
        to the client, history included. addOwners makes other Google accounts owners
        too, so the site's people keep their own access. verify_site does this for you.
        Free."""
        return self.call("verify_site_ownership", _present({"clientId": client_id, "method": method, "siteUrl": site_url, "addOwners": add_owners}))

    def whoami(self) -> Any:
        """Who am I connected as. Says who this connection is: the agency, whether it is an
        API key or a person, the role, every permission that role holds, and the clients
        it can reach. Answers 'what can this key do'. Call it first when unsure whether
        a task is allowed. Free."""
        return self.call("whoami", {})
