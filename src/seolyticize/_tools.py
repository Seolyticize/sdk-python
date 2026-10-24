# Generated from the Seolyticize tool registry. Do not edit by hand:
# regenerate with `pnpm --filter @seolyticize/sdk generate:languages`.
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

READ_ONLY_TOOLS = frozenset({
    "analyse_server_log",
    "audit_merchant_feed",
    "audit_page",
    "audit_product_page",
    "batch_domain_metrics",
    "build_disavow_file",
    "check_answer_readiness",
    "check_brand_entity",
    "check_programmatic_pages",
    "check_templated_metadata",
    "check_url_safety",
    "compare_crawls",
    "describe_datasets",
    "draft_agent_files",
    "estimate_ai_visibility_cost",
    "estimate_cost",
    "explain_keyword_difficulty",
    "export_ai_visibility_data",
    "export_data",
    "export_search_console_data",
    "export_sitemap",
    "find_journalist_requests",
    "find_tools",
    "forecast_keyword_traffic",
    "forecast_search_clicks",
    "generate_hreflang",
    "generate_llms_txt",
    "generate_schema",
    "get_agent_readiness",
    "get_ai_agent_visits",
    "get_ai_answer_share",
    "get_ai_citation_history",
    "get_ai_cited_sources",
    "get_ai_crawler_access",
    "get_ai_crawler_activity",
    "get_ai_overview_citations",
    "get_ai_referrals",
    "get_ai_visibility",
    "get_ai_visibility_answer",
    "get_ai_visibility_results",
    "get_ai_visibility_runs",
    "get_ai_visibility_sentiment",
    "get_ai_visibility_setup",
    "get_ai_visibility_trend",
    "get_anchor_overlap",
    "get_audit_performance",
    "get_audit_summary",
    "get_backlink_audit",
    "get_backlink_health",
    "get_billing",
    "get_bing_crawl_health",
    "get_bing_inbound_links",
    "get_bing_keyword_research",
    "get_bing_performance",
    "get_bing_search_stats",
    "get_brand_split",
    "get_branding",
    "get_budget_status",
    "get_cannibalization",
    "get_click_curve",
    "get_client",
    "get_client_brief",
    "get_client_costs",
    "get_client_integrations",
    "get_competitor_new_pages",
    "get_competitor_page_changes",
    "get_connection_link",
    "get_content_audit",
    "get_content_decay",
    "get_content_gap",
    "get_content_groups",
    "get_conversions",
    "get_costs",
    "get_crawl_budget",
    "get_crawl_settings",
    "get_crawl_status",
    "get_ctr_outliers",
    "get_deploy_hook",
    "get_disavow_history",
    "get_domain_facts",
    "get_domain_technologies",
    "get_engine_capabilities",
    "get_entity_pageviews",
    "get_error_catalogue",
    "get_extraction_results",
    "get_freshness_queue",
    "get_funnel_report",
    "get_ga4_audience",
    "get_ga4_ecommerce",
    "get_ga4_key_events",
    "get_ga4_landing_pages",
    "get_ga4_measurement_health",
    "get_ga4_overview",
    "get_ga4_page_performance",
    "get_ga4_site_search",
    "get_ga4_traffic_acquisition",
    "get_geo_readiness",
    "get_goal_report",
    "get_google_service_account",
    "get_hreflang_parity",
    "get_hreflang_report",
    "get_index_coverage",
    "get_indexnow_key",
    "get_internal_link_graph",
    "get_issue_templates",
    "get_job",
    "get_keyword_difficulty",
    "get_keyword_gap",
    "get_keyword_list",
    "get_landing_pages",
    "get_link_checks",
    "get_link_intersect",
    "get_link_velocity",
    "get_local_visibility",
    "get_log_orphans",
    "get_long_tail_candidates",
    "get_low_ctr_queries",
    "get_matomo_report",
    "get_media_report",
    "get_naver_keyword_volumes",
    "get_next_steps",
    "get_opportunities",
    "get_outbound_domains",
    "get_outreach_mailboxes",
    "get_outreach_status",
    "get_page_details",
    "get_page_indexing_reasons",
    "get_page_issues",
    "get_panel_reach",
    "get_parameter_report",
    "get_parasite_risk",
    "get_personal_keyword_difficulty",
    "get_portfolio_metrics",
    "get_position_distribution",
    "get_preload_readiness",
    "get_price_list",
    "get_query_intents",
    "get_query_page_swaps",
    "get_questions",
    "get_rank_history",
    "get_rank_summary",
    "get_recipe",
    "get_rendering_report",
    "get_report_data",
    "get_robots_history",
    "get_run_status",
    "get_search_anomalies",
    "get_search_appearance",
    "get_search_changes",
    "get_search_console_hourly",
    "get_search_console_performance",
    "get_search_demand",
    "get_search_opportunities",
    "get_search_timeline",
    "get_security_report",
    "get_seo_changes",
    "get_seo_revenue",
    "get_seo_scorecard",
    "get_serp_features",
    "get_serp_intent_shifts",
    "get_serp_newcomers",
    "get_serp_volatility",
    "get_share_of_search",
    "get_share_of_voice",
    "get_shopping_keyword_gap",
    "get_shopping_serp",
    "get_site_conventions",
    "get_site_status",
    "get_top_searches",
    "get_topical_authority",
    "get_toxic_link_risk",
    "get_translation_gap",
    "get_trust_signals",
    "get_url_swaps",
    "get_vendor_reconciliation",
    "get_vitals_history",
    "get_volume_calibration",
    "get_web_analytics_breakdown",
    "get_web_analytics_setup",
    "get_web_analytics_summary",
    "get_written_report",
    "get_yandex_diagnostics",
    "get_yandex_external_links",
    "get_yandex_important_pages",
    "get_yandex_indexing",
    "get_yandex_performance",
    "get_yandex_query_history",
    "get_zero_click_estimates",
    "inspect_bing_url",
    "list_accepted_issues",
    "list_alert_rules",
    "list_annotations",
    "list_client_facts",
    "list_clients",
    "list_content_plan",
    "list_conversion_goals",
    "list_crawl_issues",
    "list_crawls",
    "list_data_syncs",
    "list_digest_schedules",
    "list_funnels",
    "list_goals",
    "list_integrations",
    "list_issue_pages",
    "list_keyword_lists",
    "list_keyword_owners",
    "list_link_prospects",
    "list_local_locations",
    "list_log_sources",
    "list_markets",
    "list_outreach_sequences",
    "list_path_owners",
    "list_portfolios",
    "list_projects",
    "list_rank_trackers",
    "list_recent_alerts",
    "list_report_schedules",
    "list_report_templates",
    "list_reports",
    "list_sitemaps",
    "list_task_links",
    "list_tasks",
    "list_tracked_keywords",
    "list_written_reports",
    "page_vitals",
    "plan_redirect_map",
    "preview_weekly_digest",
    "propose_keyword_owners",
    "query_data",
    "query_keyword_list",
    "score_eeat",
    "search_locations",
    "simulate_serp_snippet",
    "striking_distance",
    "suggest_internal_links",
    "sync_search_console",
    "test_robots",
    "validate_product_schema",
    "validate_sitemap",
    "validate_structured_data",
    "wait_for_job",
    "whoami",
})

TOOL_COUNT = 499


def _present(values: Dict[str, Any]) -> Dict[str, Any]:
    """Drops arguments left as None, so the server applies its own defaults."""
    return {key: value for key, value in values.items() if value is not None}


class Tools:
    """One method per tool. Every argument is keyword-only, named in snake_case."""

    def call(self, tool: str, input: Optional[Dict[str, Any]] = None) -> Any:  # pragma: no cover
        raise NotImplementedError

    def accept_issue(self, *, client_id: str, rule_id: str, reason: str, template: Optional[str] = None, urls: Optional[List[str]] = None, until: Optional[str] = None, dry_run: Optional[bool] = None) -> Any:
        """Accept an audit issue as intentional. Marks one audit rule's findings as kept on
        purpose, on the pages of a URL template (template: /login, /legal/*,
        /docs/*?sort=*; * is one path segment, a final ** the rest; a template without a
        query matches any query) or on listed addresses (urls), with the reason and,
        optionally, the last day it holds (until, YYYY-MM-DD). From then on those
        findings leave get_seo_scorecard, the counts of get_audit_summary (shown apart
        as accepted, each with its reason), the weekly digest, create_tasks_from_audit
        and the alerts; list_issue_pages marks them. ruleId comes from
        get_audit_summary. matchedNow is how many of the latest crawl's findings of the
        rule it covers, out of rulePages (both null without a crawl), with a sample of
        the covered addresses; warning is set when it covers nothing, or when a template
        covers more than half the rule's pages (likely too broad). dryRun: true saves
        nothing and answers the same coverage, to check a template first. Examples:
        login pages noindexed by design, old versions of the legal pages, sort variants.
        unaccept_issue undoes it. Answers 'stop flagging our login pages, they are
        noindexed on purpose'. Free."""
        return self.call("accept_issue", _present({"clientId": client_id, "ruleId": rule_id, "template": template, "urls": urls, "reason": reason, "until": until, "dryRun": dry_run}))

    def add_annotation(self, *, client_id: str, on: str, kind: Literal["deploy", "publish", "content_update", "campaign", "technical", "note"], title: str, detail: Optional[str] = None, url: Optional[str] = None) -> Any:
        """Note something on the client's timeline. Records something that happened on a
        day — a deploy, a page published or rewritten, a campaign, a technical change, a
        note — so traffic charts and get_search_timeline can be read as cause and
        effect. Answers 'remember that we shipped this today'. Deploy hooks note their
        runs on their own. Free."""
        return self.call("add_annotation", _present({"clientId": client_id, "on": on, "kind": kind, "title": title, "detail": detail, "url": url}))

    def add_competitors(self, *, client_id: str, tracker_id: str, domains: List[str]) -> Any:
        """Add competitors to a tracker. Adds competitor domains to a rank tracker, so
        share of voice and the competitor comparisons measure them on the same keywords.
        Answers 'compare us with these sites'. Returns the tracker's full competitor
        list. Domains already there are left as they are."""
        return self.call("add_competitors", _present({"clientId": client_id, "trackerId": tracker_id, "domains": domains}))

    def add_default_alerts(self, *, client_id: Optional[str] = None, all_clients: Optional[bool] = None) -> Any:
        """Add the default alerts. Gives a client the four alerts every new client now
        starts with: the site goes down (site-unreachable), non-branded Search Console
        clicks fall 30% or more week on week (traffic-drop 30), a crawl finds critical
        issues (new-critical-issues 1), and a tracked keyword drops 5 or more places
        (rank-drop 5). Each goes to the agency owner's email until changed with
        update_alert_rule. A kind the client already has a rule for is kept as it is, so
        it is safe to repeat. Pass clientId for one client, or allClients: true for
        every live client the key may manage. Answers 'set up the usual alerts'. Free."""
        return self.call("add_default_alerts", _present({"clientId": client_id, "allClients": all_clients}))

    def add_keywords_to_list(self, *, list_id: str, keywords: List[Dict[str, Any]]) -> Any:
        """Add keywords to a list. Adds keywords to an existing list. Keywords already on
        it are counted as already present and otherwise left alone, except that metrics
        passed with them replace the fields given. Answers 'save these to that list'.
        Each keyword may carry the metrics keyword_explorer or get_keyword_metrics
        already returned (volume, difficulty, CPC in micro-USD, intent, SERP features);
        they are stored with their read time, so refresh_keyword_list_metrics need not
        buy them again. Location code defaults to 2840 (United States), language to en,
        engine to google."""
        return self.call("add_keywords_to_list", _present({"listId": list_id, "keywords": keywords}))

    def add_link_prospects(self, *, client_id: str, prospects: List[Dict[str, Any]]) -> Any:
        """Add sites to a client's outreach list. Adds linking-site prospects to the
        client's outreach list at the identified stage — typically the domains
        get_link_intersect finds linking to competitors but not the client, with that as
        the reason. Give targetUrl when the prospect is one page — a dead page to
        reclaim, a thread to answer, an article that mentions the brand — so each page
        is its own row; without it the prospect is the whole site. A site or page
        already on the list is left at its current stage, never reset. Answers 'add
        these sites to our outreach'. Free."""
        return self.call("add_link_prospects", _present({"clientId": client_id, "prospects": prospects}))

    def add_list_to_tracker(self, *, client_id: str, tracker_id: str, list_id: str) -> Any:
        """Track a keyword list. Adds every keyword on a list to one of the client's rank
        trackers. Answers 'start tracking everything on that list'. Keywords for another
        country, language or engine than the tracker reads are skipped and listed with
        the reason, never tracked in the wrong market. Each added keyword is a paid
        lookup on every future run, so quote the tracker with estimate_cost afterwards
        if cost matters; refused when the plan's keyword allowance would be exceeded."""
        return self.call("add_list_to_tracker", _present({"clientId": client_id, "trackerId": tracker_id, "listId": list_id}))

    def add_local_location(self, *, client_id: str, name: str, lat: float, lng: float, place_id: Optional[str] = None, cid: Optional[str] = None) -> Any:
        """Add a business location. Adds a business location to a client for local SEO, at
        a latitude and longitude — the centre of every grid scan around it. Give its
        Google placeId (or cid) when known — get_business_profile finds both, with the
        coordinates — so scans match the listing itself, not any business with the same
        name. Answers 'start tracking this branch in the map pack'. Free."""
        return self.call("add_local_location", _present({"clientId": client_id, "name": name, "lat": lat, "lng": lng, "placeId": place_id, "cid": cid}))

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
        crawler requests that returned no content), aiCrawlerShare, aiByPurpose (AI
        agents' requests split into training crawls — GPTBot, ClaudeBot, CCBot, Meta,
        Bytespider, Amazonbot — search indexing — OAI-SearchBot, Claude-SearchBot,
        PerplexityBot, Applebot, DuckAssistBot — and user fetches — ChatGPT-User,
        Claude-User, Perplexity-User, MistralAI-User, an assistant reading the page
        because someone asked it something), aiUserPaths (the pages assistants fetched
        for people: the nearest a log gets to citations), totalHits and totalBytes. Also
        linesRead, linesUnparsed (lines in a format it did not recognise — many means
        the wrong format, not a quiet site), humanHits and truncated. Up to 64 MB per
        call; split a bigger log and call once per part. Nothing is stored. Answers
        'what is Googlebot actually crawling on our site' and 'which of our pages are AI
        assistants reading'. Free."""
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

    def assess_ai_visibility_sentiment(self, *, client_id: str, captured_at: Optional[str] = None, max_answers: Optional[int] = None, rejudge: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Judge sentiment for answers already captured. Judges how each answer in one
        check (the latest unless capturedAt names one) describes the tracked brands it
        names, for answers not yet judged — those captured before sentiment was on, or
        when the judge was unavailable. One metered Claude call per answer, up to
        maxAnswers (default 50); rejudge: true judges again. Returns judged, skipped,
        left and costMicros. Get the user's go-ahead first: it spends. Answers 'fill in
        sentiment for last week's check'. Can spend: pass max_cost_micros to cap it."""
        return self.call("assess_ai_visibility_sentiment", _present({"clientId": client_id, "capturedAt": captured_at, "maxAnswers": max_answers, "rejudge": rejudge, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def audit_merchant_feed(self, *, client_id: str, merchant_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Audit the Merchant Center product feed. Reads the client's connected Google
        Merchant Center account (Merchant API) and audits its products: Google's own
        item-level issues grouped by code, worst first (disapproved, then demoted), with
        how many products each hits, examples and Google's help link; approval counts
        per destination; and what Google does not flag but Shopping placement rewards —
        titles too short or without the brand, thin descriptions, missing GTINs, single
        images, out of stock. Answers 'why are our products disapproved' and 'how good
        is our feed'. Needs Merchant Center connected (get_connection_link names the
        link; /api/connect/merchant/start). Free."""
        return self.call("audit_merchant_feed", _present({"clientId": client_id, "merchantId": merchant_id, "limit": limit}))

    def audit_page(self, *, client_id: str, url: str, render: Optional[Literal["off", "auto"]] = None, page_type: Optional[Literal["home", "service", "location_primary", "location_secondary", "blog", "product", "category", "about", "landing", "faq", "other"]] = None) -> Any:
        """Audit one page. Fetches one page of the client's site now and runs the crawler's
        full rule engine over it, plus page-level thresholds: title 30–60 characters,
        meta description 120–160, exactly one H1 and no skipped heading levels,
        og:title, og:description, og:image and og:url, twitter:card, twitter:title and
        twitter:description, alt text 10–125 characters, images over 200KB (warning) or
        500KB (critical), and a word-count floor for the page type (home 500, service
        800, primary location 600, secondary location 500, blog 1,500, product, category
        and about 400, landing 600, FAQ 800; pageType overrides the guess from the URL
        and markup), Flesch reading ease (60–70 suits a general audience; only under 30
        is flagged, since it is not a ranking factor), query parameters in the URL
        (tracking parameters aside), links from the copy itself to the site's own pages
        against the page type's target (blog 5–10, service 3–5, product 2–4; navigation,
        header and footer links not counted), and templated metadata (a description that
        restates the title, closes on a stock call to action or repeats the title's
        brand suffix). Returns an overall score and five sub-scores (on-page, content,
        technical, schema, images; null where not measured), every issue by severity
        with its fix, and generate_schema's suggestions for the page. render 'auto'
        renders the page in a browser when its HTML looks like an unrendered shell. A
        heuristic. Answers 'what is wrong with this page' and 'is this page ready'.
        Free."""
        return self.call("audit_page", _present({"clientId": client_id, "url": url, "render": render, "pageType": page_type}))

    def audit_product_page(self, *, client_id: str, url: str, manufacturer_text: Optional[str] = None) -> Any:
        """Audit one product page. Reads one product page now and scores it 0–100 (a
        heuristic, said so in the answer) from six weighted parts, each check pass, warn
        or fail with the reason, or null when it cannot be judged (then left out and the
        weights rescaled): Product schema (25, the completeness validate_product_schema
        gives), title and meta (15: a title under 60 characters, a meta description
        under 155 with a price and a call to action), images (20: at least 3, each at
        least 50,000 pixels where the page declares sizes, alt text), content (20: 200
        words or more, not the manufacturer's copy — pass manufacturerText to compare —
        a specifications table, reviews), linking (10: breadcrumbs, a link to its
        category, related products) and technical (10: status 200, indexable, a self
        canonical, a viewport, HTTPS). Answers 'what is wrong with this product page'
        and 'why does this product not rank'. Free."""
        return self.call("audit_product_page", _present({"clientId": client_id, "url": url, "manufacturerText": manufacturer_text}))

    def batch_domain_metrics(self, *, domains: List[str]) -> Any:
        """Look up domains in bulk. Authority, keywords, traffic and referring domains for
        any list of domains, managed or not. Answers 'how strong is this site' for
        competitors and prospects."""
        return self.call("batch_domain_metrics", _present({"domains": domains}))

    def build_comparison_page(self, *, client_id: str, page_type: Literal["vs", "alternatives", "roundup", "table"], competitors: List[Dict[str, Any]], features: Optional[List[str]] = None, source_urls: Optional[List[str]] = None, category: Optional[str] = None, demand: Optional[bool] = None, instructions: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Build a comparison page. Plans an honest comparison page — vs (the client
        against one rival), alternatives (to the first competitor), roundup (best tools
        in a category) or table — from what each product publishes: its pricing and
        feature pages (and any sourceUrls) are read and a feature matrix filled, each
        cell ✅, ⚠️ partial, ❌ or 'Not publicly available' with its source URL, and every
        price 'as of' the read. Gives the title from the pageType's template, an H1
        under 70 characters, a sourced outline of at least 1,500 words with calls to
        action above the fold, after the table and at the end (never inside a
        competitor's section), each competitor's strengths acknowledged, the client's
        product named as the client's, JSON-LD (SoftwareApplication with offers;
        ItemList in ranked order for roundups; no AggregateRating without real review
        data) checked against Google's requirements; each product's hidden costs from
        its pricing page (setup fees, per-user pricing, overages, transaction fees,
        annual-only billing, minimum seats), a 'Last updated' stamp, related comparisons
        to link, and checks that the outline carries a methodology section, the hidden
        costs and related comparisons; and the comparison searches by pattern ('[a] vs
        [b]', '[a] vs [b] pricing', 'is [a] better than [b]', '[a] alternatives', '[a]
        alternatives [year]', '[a] review [year]', 'best [category] tools', '[category]
        comparison'), with demand: true their volumes (one paid keyword-metrics read).
        Answers 'write a vs page against our rival' and 'what should our alternatives
        page say'. The outline is one metered Claude call; quote with estimate_cost. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("build_comparison_page", _present({"clientId": client_id, "pageType": page_type, "competitors": competitors, "features": features, "sourceUrls": source_urls, "category": category, "demand": demand, "instructions": instructions, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def build_content_brief(self, *, client_id: str, keyword: str, related_keywords: Optional[List[str]] = None, target_url: Optional[str] = None, page_type: Optional[Literal["service", "blog", "case_study", "category", "landing", "faq", "location", "about", "homepage"]] = None, depth: Optional[int] = None, save: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Build a content brief. A writer's brief for a keyword (or a cluster: the keyword
        plus relatedKeywords), built from the pages that rank: search intent and the
        format that wins (list, how-to, comparison, review, landing page, article),
        target length, the outline to cover, must-cover and nice-to-have terms,
        questions to answer (People Also Ask and the ranking pages'), structure and
        schema to include, the client's own pages to link to and from, and each
        competing page with what it misses — and ownership, a warning for each keyword
        the keyword registry already gives another page ('this already belongs to /x').
        Also: each competitor scored 1–10 on depth, format, SEO and UX (out of 40), with
        claude-seo's full excluded list left out as non-competitors (encyclopedias,
        social and content platforms, search engines, marketplaces, forums, news and
        media, data platforms, directories, comparison aggregators, job boards, SEO
        tools, AI platforms, government and academic domains, and tag, author, login,
        legal and feed paths on any domain), and thinCompetition set when fewer than 3
        real competitors remain; a section template for the page type (pageType:
        service, blog, case_study, category, landing, faq, location, about or homepage;
        default from the intent) with its goal, sections, schema (never FAQPage) and
        keyword placement; gaps typed topic, depth or quality with priority = impact ×
        advantage ÷ effort; a required information-gain statement; the E-E-A-T the page
        needs; words per section; the featured-snippet section and format; title 50–60
        and description 130–150 character targets; and with targetUrl, improve mode
        marking each section keep, strengthen or add against the page as it stands.
        Answers 'brief me on this keyword' and 'what should this post cover'. save: true
        keeps it as a research note on the client brief. Same cost as
        get_serp_content_profile. Can spend: pass max_cost_micros to cap it."""
        return self.call("build_content_brief", _present({"clientId": client_id, "keyword": keyword, "relatedKeywords": related_keywords, "targetUrl": target_url, "pageType": page_type, "depth": depth, "save": save, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def build_disavow_file(self, *, entries: List[Dict[str, Any]]) -> Any:
        """Build a disavow file. Builds a Google disavow file from domains and URLs: a
        domain entry disavows every link from that domain, a url entry names one page.
        Answers 'make the disavow file for these links'. Free; nothing is submitted —
        Google takes the file by upload in Search Console, which a person does. Use
        get_backlink_audit to find the links worth disavowing, and have a person review
        every line first: disavowing a good link removes value the client earned.
        Malformed entries are left out rather than written."""
        return self.call("build_disavow_file", _present({"entries": entries}))

    def capture_page_screenshots(self, *, client_id: str, url: str, viewports: Optional[List[Literal["1920x1080", "1366x768", "768x1024", "375x812"]]] = None, parity: Optional[bool] = None) -> Any:
        """Screenshots and layout checks at four screen sizes. Renders one of the client's
        pages in a real browser at 1920×1080, 1366×768, 768×1024 and 375×812 (viewports
        narrows it), stores a PNG of each first screen (links last a day) and checks the
        layout there: whether the H1, the primary call to action and the hero image are
        above the fold, horizontal scrolling, tap targets under 24×24 px (fail) and
        under 48×48 (warn) — inline text links excepted — the base font size under 16px,
        overlapping controls and clipped text, and a fixed overlay covering over half
        the screen on load (cookie and consent banners excepted). parity (default on)
        also fetches the page as Googlebot smartphone and as desktop Chrome and compares
        words, links, headings and structured data types, since Google indexes the
        mobile version. Answers 'does the page work on a phone', 'is the CTA above the
        fold' and 'does Google's mobile crawler see the same page'. No vendor charge; it
        renders pages on the client's behalf, so it needs project:manage."""
        return self.call("capture_page_screenshots", _present({"clientId": client_id, "url": url, "viewports": viewports, "parity": parity}))

    def check_ai_brand_accuracy(self, *, client_id: str, facts: Optional[List[str]] = None, question: Optional[str] = None, platforms: Optional[List[Literal["chat_gpt_app", "perplexity", "chat_gpt", "claude", "gemini"]]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Do assistants describe the brand correctly. Asks assistants about the client's
        brand now (the ChatGPT app and Perplexity by default, or chat_gpt, claude,
        gemini) and checks every claim they make against the facts given — or, by
        default, the client's registered facts (set_client_facts), and failing those the
        client brief's overview and positioning — each claim marked supported,
        contradicted or unverified (the facts do not say), with the fact that decides
        it. Answers 'what does ChatGPT get wrong about us' and 'is the AI description of
        our brand accurate'. Paid: the live answers on DataForSEO plus a metered Claude
        call; quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("check_ai_brand_accuracy", _present({"clientId": client_id, "facts": facts, "question": question, "platforms": platforms, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def check_answer_readiness(self, *, client_id: str, urls: Optional[List[str]] = None, top_pages: Optional[int] = None) -> Any:
        """Is the page written to be quoted by assistants. Checks pages of the client's
        site for what makes an assistant quote them: a direct answer in the first 100
        words (not a preamble), a plain definition, sourced claims (links to sources
        outside the site, against the figures stated), a named author, a published or
        updated date, and structured data — a 0–100 score and a fix list per page, and
        the site's fixes in order of how many pages need them. Give urls, or check the
        top pages by Search Console clicks (topPages). Answers 'why is this page not
        cited' and 'how do we make our pages answer-ready'. Free."""
        return self.call("check_answer_readiness", _present({"clientId": client_id, "urls": urls, "topPages": top_pages}))

    def check_brand_entity(self, *, client_id: str, brand: Optional[str] = None, languages: Optional[List[str]] = None) -> Any:
        """Does Google know the brand as an entity. Looks the client's brand (default its
        name) up in Google's Knowledge Graph Search API: whether there is an entity for
        it, its types, description, Wikipedia article and official URL, whether that URL
        is the client's own site, and how far it scores ahead of the next candidate —
        matched, ambiguous or absent — with what to do about each (Organization schema
        with sameAs, a Wikidata item, one consistent name). Answers 'does Google have a
        knowledge panel entity for us' and 'is our brand an entity'. Free."""
        return self.call("check_brand_entity", _present({"clientId": client_id, "brand": brand, "languages": languages}))

    def check_deploy(self, *, client_id: str, preview_url: Optional[str] = None, urls: Optional[List[str]] = None, max_urls: Optional[int] = None, fail_on: Optional[Literal["critical", "warning", "notice"]] = None, baseline_crawl_id: Optional[str] = None) -> Any:
        """Check a deploy before it ships. Fetches pages now and compares what they tell
        search engines (status, robots, canonical, hreflang, title, H1, structured data
        types; and, against crawls that recorded them, meta description, Open Graph
        tags, structured data values, H2 outline and copy) with the latest complete
        crawl's snapshot of the same paths, or the complete crawl baselineCrawlId names
        (from list_crawls), to compare against a crawl from before a release; baseline
        says which crawl was used and when it ran, and notes warns when the latest crawl
        started before the last recorded deploy (deploy hook or deploy annotation), so
        the baseline may already include that release. Give previewUrl (a deploy preview
        or staging origin: the crawl's pages, one or more per template, are fetched on
        that host, up to maxUrls) or urls (specific addresses, on production or a
        preview; matched by path). Canonicals and hreflang on the preview host are read
        as the production host, so only real changes show. passed is false when anything
        at or above failOn (default critical: noindex added, canonical changed, title
        dropped, a page now 4xx/5xx, hreflang lost, a page unreachable) changed;
        markdown is a ready pull-request comment. The client's set_crawl_auth
        credentials are sent to the preview host too, so a password-protected preview
        can be checked. Used by the Seolyticize GitHub Action. Answers 'will this deploy
        hurt SEO' and 'did the release noindex anything'. No vendor charge; it fetches
        pages on the client's behalf, so it needs project:manage."""
        return self.call("check_deploy", _present({"clientId": client_id, "previewUrl": preview_url, "urls": urls, "maxUrls": max_urls, "failOn": fail_on, "baselineCrawlId": baseline_crawl_id}))

    def check_nap_consistency(self, *, client_id: str, location_id: str, use_listing: Optional[bool] = None, directories: Optional[bool] = None, industry_directories: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Do the site and the Google listing agree. Compares the business's name, address
        and phone on its Google listing with what its site says — the homepage and its
        contact, about and location pages, text and structured data — and says which
        agree, which differ and how. Inconsistent details weaken local rankings and
        confuse assistants. useListing reads the live Google listing (paid, by place id)
        instead of the location as saved. directories also audits citations: Google is
        searched for the business's name and phone on Yelp, Foursquare, Facebook, Yellow
        Pages, Superpages, BBB, Tripadvisor, MapQuest, Apple Maps, Nextdoor and more,
        plus the trade's own directories (industryDirectories, detected when not given),
        and each directory's name, address and phone as shown is compared with the
        listing (null where the result did not show it), with a severity for the worst
        disagreement — a different name critical, address warning, phone notice;
        directories with no listing found are named. Bing Places and Apple Business
        Connect have no self-serve API, so neither is read directly. Answers 'is our NAP
        consistent' and 'which directories list us wrongly'. Free with the saved
        location; quote useListing and directories (two results pages) with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("check_nap_consistency", _present({"clientId": client_id, "locationId": location_id, "useListing": use_listing, "directories": directories, "industryDirectories": industry_directories, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def check_programmatic_pages(self, *, client_id: str, crawl_id: Optional[str] = None, template: Optional[str] = None, min_variants: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Do the template pages earn their place. Finds the site's template pages (the
        same path with one variable segment, minVariants or more of them; or one
        template given as a glob such as /sms/*) in a crawl and, for every variant: how
        much of its text is its own (the share no more than a third of its siblings
        repeat) and how close its nearest sibling is (simhash bits), whether it is thin
        against the template's median, and its demand (Search Console clicks and
        impressions over 90 days, stored search volume for its H1) — with a verdict:
        keep, merge (all but a duplicate of a sibling with more demand: fold it in) or
        noindex (thin or boilerplate, and no demand). Each template also gets checks
        with six 0–100 sub-scores (data, template uniqueness, URL, linking, thin risk,
        index management; null where unmeasured): a gate (100+ unreviewed pages is a
        warning, 500+ says stop), thin content (under 40% own text is thin, under 30%
        fails, under 300 words flagged), descriptions that open with the title, end on a
        stock call to action or share one shape with the name swapped in, URL rules
        (lowercase, hyphens, under 100 characters, no query string, one trailing-slash
        style, no duplicate slugs), links to 3–5 siblings, self-referencing canonicals,
        and Google's indexing (URL Inspection) against the pages meant to be indexed.
        checks.extras adds near-duplicate records (title, H1 and description sharing
        more than 80% of their words), boilerplate (pages whose copy is over 60% words
        most of the template's pages share), a review sample of 5% of the template,
        thinnest first (up to 10% is better), noindexed variants the sitemaps still
        list, and a crawl-budget notice past 10,000 pages. Answers 'which of our
        location pages should exist' and 'are these programmatic pages thin'. For the
        demand of combinations not yet built, use get_demand_matrix. Free."""
        return self.call("check_programmatic_pages", _present({"clientId": client_id, "crawlId": crawl_id, "template": template, "minVariants": min_variants, "limit": limit}))

    def check_shopping_serp(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Queue Google Shopping results for keywords. Queues a Google Shopping results
        page for each keyword (up to 20) at DataForSEO, which answers in a few minutes;
        collect them with get_shopping_serp and the task ids returned. Answers 'track
        our Google Shopping positions'. One purchase per keyword. A paid lookup on the
        client's account (spend says how much); quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("check_shopping_serp", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def check_templated_metadata(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """Descriptions a template wrote. Reads every crawled page's title and meta
        description (latest crawl, or crawlId) for the shapes bulk generation leaves: a
        description that opens by restating its own title and closes on a stock call to
        action ('Try it free now.', 'Get started today!'; templated, high), one that
        only echoes the title (medium), the title's brand suffix pasted into the
        description (low), and a description that is the title again (medium). Site risk
        is high when 3 or more pages and at least 30% of those checked are templated,
        medium from 10%; a stock closer shared by 3 or more pages is flagged too.
        Returns the counts, the shared closers, and the flagged pages worst first with a
        fix each. Deterministic string comparison: a heuristic, which claims no Google
        update targeted the pattern. Answers 'are our meta descriptions templated' and
        'which descriptions should we rewrite'. Free."""
        return self.call("check_templated_metadata", _present({"clientId": client_id, "crawlId": crawl_id}))

    def check_url_safety(self, *, client_id: str, urls: Optional[List[str]] = None, outbound: Optional[bool] = None) -> Any:
        """Is the site, or a site it links to, flagged as unsafe. Looks up the client's
        homepage, the addresses given, and (outbound, on by default) the external sites
        its homepage links to on Google's Web Risk lists — malware, social engineering
        (phishing) and unwanted software — and says which are flagged, with the threat
        types and until when the match holds. A flagged own page is what turns into a
        browser warning and lost traffic; a flagged outbound link is a hacked partner or
        a planted spam link. Answers 'has our site been flagged by Google as unsafe' and
        'do we link to any malware sites'. Free."""
        return self.call("check_url_safety", _present({"clientId": client_id, "urls": urls, "outbound": outbound}))

    def cluster_keywords(self, *, client_id: str, keywords: Optional[List[str]] = None, list_id: Optional[str] = None, min_shared: Optional[int] = None, depth: Optional[int] = None, mode: Optional[Literal["head", "connected"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Group keywords into topics. Groups keywords into topics by how much their Google
        results overlap: keywords whose top results share at least minShared pages are
        one topic, which one page should target. Each topic has its parent topic (the
        highest-volume keyword), total volume, intent, the pages that rank across it,
        and where the client already ranks. overlap lists keyword pairs by shared
        top-ten results: 7–10 merge (one page), 4–6 same cluster, 2–3 interlink, 0–1
        separate, after leaving out up to the 5 commonest domains that rank on over half
        the results pages (Wikipedia, Reddit and the like). architecture leaves
        navigational keywords out and lays the topics out as one pillar (2,500–4,000
        words) with 2–5 clusters of 2–4 spokes (1,200–1,800 words), one of eight
        templates picked by intent and wording (ultimate guide, how-to, listicle,
        explainer, comparison, review, best-of, landing page), a link matrix {from, to,
        type, anchor} whose anchors vary so no one carries over 40% of a page's inbound
        links: spoke ↔ pillar mandatory, 2–3 spoke-to-spoke, at most one cross-cluster,
        at least 3 inbound per post, every post within 2 clicks of the pillar, 5–21
        posts in all, and JSON-LD for the pillar (Article, BreadcrumbList, ItemList of
        spokes) and each spoke (Article isPartOf the pillar). scorecard checks the
        client's live pages against it from the latest crawl: no orphans, pillar links
        100% both ways, 80% of the planned links present. Answers 'which of these
        keywords belong on one page' and 'how many pages do we need'. Give keywords (up
        to 200) or a keyword listId. One results page per keyword, each a paid lookup on
        the client's account unless someone bought it in the last day — quote with
        estimate_cost first. Can spend: pass max_cost_micros to cap it."""
        return self.call("cluster_keywords", _present({"clientId": client_id, "keywords": keywords, "listId": list_id, "minShared": min_shared, "depth": depth, "mode": mode, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def compare_crawls(self, *, client_id: str, crawl_id: Optional[str] = None, against_crawl_id: Optional[str] = None, sample: Optional[int] = None) -> Any:
        """What changed since the last crawl. Compares a crawl's issues with the crawl
        before it (or againstCrawlId), page by page: issues that are new, issues that
        were fixed, and checks whose count went up (regressed) or down (improved) — a
        check that flagged a few new pages while clearing more counts as improved — or
        stayed level with different pages (shifted), each with the pages that came and
        went — plus pages added, removed and changed. Answers 'did the fixes work',
        'what broke this week' and 'what should the weekly audit report'. Free."""
        return self.call("compare_crawls", _present({"clientId": client_id, "crawlId": crawl_id, "againstCrawlId": against_crawl_id, "sample": sample}))

    def compare_sites(self, *, client_id: str, a: str, b: str, paths: Optional[List[str]] = None, max_pages: Optional[int] = None, send_crawl_auth_to: Optional[Literal["a", "b", "none"]] = None, follow_redirect: Optional[bool] = None) -> Any:
        """Compare staging with production. Fetches the same paths on two origins — staging
        (a) and production (b), say — and lists every difference in what they tell
        search engines: status, robots, canonical (read on each side's own host),
        hreflang, title, H1 and structured data, with critical ones first and a Markdown
        summary. Paths default to the client's latest crawl (its shallowest pages,
        spread across templates) or, without a crawl, the links on b's home page; paths
        narrows it. sendCrawlAuthTo sends the client's set_crawl_auth credentials (basic
        auth, headers, cookies) to that side only, for a password-protected staging
        site. When one side's home redirects to the other's host (www to the apex),
        redirect names the status and target and nothing is diffed, since that side has
        no pages of its own; single paths that redirect across are listed in redirected.
        followRedirect: true follows that redirect instead of stopping: each path on the
        redirecting side is fetched to where it lands and compared with the same path on
        the other side (the redirect's destination), redirectMap lists where each
        landed, and a path the redirect sends elsewhere (the home page, a 404) or a
        temporary redirect shows as a change; redirect stays reported and
        followedRedirect says it was followed. Answers 'is staging ready to go live',
        'what will the migration change' and 'does www still redirect every page to the
        same path'. No vendor charge; it fetches pages on the client's behalf, so it
        needs project:manage."""
        return self.call("compare_sites", _present({"clientId": client_id, "a": a, "b": b, "paths": paths, "maxPages": max_pages, "sendCrawlAuthTo": send_crawl_auth_to, "followRedirect": follow_redirect}))

    def connect_google_analytics_service_account(self, *, client_id: str, property_id: str) -> Any:
        """Connect GA4 by service account. Connects a client's GA4 property as the agency's
        Google service account, once the property's owner has added that address with
        the Viewer role. Answers 'they added our address in GA4, connect it'. propertyId
        is GA4's numeric property id (Admin → Property details), not a G- measurement
        id. Access is checked with Google first, and refused with the exact steps when
        it is not granted yet. Free."""
        return self.call("connect_google_analytics_service_account", _present({"clientId": client_id, "propertyId": property_id}))

    def connect_integration(self, *, client_id: str, provider: Literal["airtable", "slack", "discord", "telegram", "jira", "linear", "github", "matomo"], token: Optional[str] = None, webhook_url: Optional[str] = None, channel: Optional[str] = None, chat_id: Optional[str] = None, site: Optional[str] = None, email: Optional[str] = None, project_key: Optional[str] = None, issue_type: Optional[str] = None, team_id: Optional[str] = None, owner: Optional[str] = None, repo: Optional[str] = None, id_site: Optional[str] = None) -> Any:
        """Connect Slack, Discord, Telegram, Airtable, a tracker or Matomo. Connects one of
        the client's own tools by token. Slack: webhookUrl (an incoming webhook), or
        token (a bot token, xoxb-…) with channel. Discord: webhookUrl. Telegram: token
        (from BotFather) with chatId. Airtable: token (a personal access token with
        data.records:read and write on the base). Jira: site (https://….atlassian.net),
        email, token (an API token), projectKey, optional issueType. Linear: token (a
        personal API key) and teamId. GitHub: token (fine-grained, Issues read and
        write), owner and repo. Matomo (analytics instead of GA4): site (the Matomo
        address, https://…), idSite (the site's id in Matomo) and token (a token_auth
        with view access, from Administration → Personal → Security; a POST-only token
        works); read with get_matomo_report. Checked with one call, then sealed. For
        Linear and GitHub it returns a webhook URL and secret to add in the tracker for
        instant status sync (polling hourly works without). Answers 'post the digest to
        our Slack', 'mirror tasks into Jira'. Free."""
        return self.call("connect_integration", _present({"clientId": client_id, "provider": provider, "token": token, "webhookUrl": webhook_url, "channel": channel, "chatId": chat_id, "site": site, "email": email, "projectKey": project_key, "issueType": issue_type, "teamId": team_id, "owner": owner, "repo": repo, "idSite": id_site}))

    def connect_log_source(self, *, client_id: str, kind: Literal["cloudflare-logpush", "cloudflare-worker", "vercel", "fastly", "s3", "upload"], label: Optional[str] = None, s3: Optional[Dict[str, Any]] = None, vercel_verify: Optional[str] = None) -> Any:
        """Connect a server log feed. Connects a feed of the client's access logs so
        crawler reports stay current without uploads. kind: cloudflare-logpush (an HTTP
        destination for a Logpush http_requests job), cloudflare-worker (a Worker
        snippet for zones without Logpush), vercel (a log drain), fastly (an HTTPS
        logging endpoint, with the JSON format string to use), s3 (a bucket and prefix
        the worker pulls new objects from every hour — combined log format or Logpush
        NDJSON, gzipped or not; give s3 with read-only keys, stored encrypted) or upload
        (a URL to POST log files to). Returns the ingest URL (shown once: it carries the
        secret), the setup steps and any snippet. Only crawler requests are kept —
        visitors' requests are counted and dropped — and each crawler's claim is checked
        against reverse DNS or its published IP ranges. Answers 'stream our Cloudflare
        logs in' and 'set up a Vercel log drain'. Free."""
        return self.call("connect_log_source", _present({"clientId": client_id, "kind": kind, "label": label, "s3": s3, "vercelVerify": vercel_verify}))

    def connect_revenue_source(self, *, client_id: str, provider: Literal["stripe", "shopify", "paddle"], api_key: Optional[str] = None, shop: Optional[str] = None, access_token: Optional[str] = None, sandbox: Optional[bool] = None) -> Any:
        """Connect Stripe, Shopify or Paddle. Connects the client's own store so its orders
        can be counted against SEO. Stripe: a restricted key (rk_…) with read access to
        Charges and PaymentIntents — or use get_integration_connect_link for Stripe
        Connect. Shopify: the store's myshopify.com domain and a custom app's Admin API
        access token with read_orders — or the connect link for OAuth. Paddle: an API
        key with transaction.read (sandbox: true for a sandbox account). The key is
        checked, sealed, and the last 90 days imported straight away. Answers 'connect
        the client's Shopify'. Free."""
        return self.call("connect_revenue_source", _present({"clientId": client_id, "provider": provider, "apiKey": api_key, "shop": shop, "accessToken": access_token, "sandbox": sandbox}))

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

    def create_alert_rule(self, *, client_id: str, kind: Literal["rank-drop", "traffic-drop", "new-critical-issues", "backlinks-lost", "site-unreachable", "serp-features", "competitor-new-pages", "page-changes", "ai-mention-drop", "competitor-new-keywords", "web-mentions", "link-velocity"], threshold: int, cooldown_hours: Optional[int] = None, webhook_url: Optional[str] = None, channel: Optional[Literal["slack", "webhook", "email", "telegram"]] = None, email_recipients: Optional[List[str]] = None, telegram_chat_id: Optional[str] = None, paid_source: Optional[bool] = None) -> Any:
        """Create an alert rule. Raises an alert when a client's rankings, traffic, issues
        or backlinks cross a threshold, or the site goes down, and delivers it by
        channel. Threshold by kind: rank-drop positions fallen; traffic-drop percent
        lost; new-critical-issues and backlinks-lost a count; serp-features features
        lost (or won); competitor-new-pages new pages one tracked competitor's sitemap
        gained; page-changes own pages whose title, meta description, H1 or canonical
        changed, went noindex or 404 between the last two audits; ai-mention-drop
        percentage points the client's AI mention or citation rate fell from the
        previous check; competitor-new-keywords tracked keywords one competitor started
        ranking for; web-mentions new pages our crawl found naming the brand;
        link-velocity referring domains gained or lost in one day, far above that
        domain's own baseline, for the client or a tracked competitor. The watch kinds
        look back to their last firing (a week at most) and stay silent until there is
        something to compare. Channels: slack (webhookUrl, Slack's format; the default),
        webhook (webhookUrl, plain JSON), email (emailRecipients, up to ten) or telegram
        (telegramChatId, with the agency's bot from Settings). Webhooks must be https
        and public. With no channel and no destination, the alert goes to the agency
        owner's email and deliveryNote says so; a channel named without its field is
        refused as no_delivery_target. paidSource (competitor-new-keywords and
        web-mentions only; off by default; needs spend permission) also buys the signal
        from DataForSEO on every sweep: for competitor-new-keywords, Labs ranked
        keywords each tracker competitor (up to 5) newly ranks for at the tracker's
        market, not only tracked keywords; for web-mentions, pages DataForSEO's content
        index first saw naming the brand, off the client's own domains. The sweep is
        hourly but a purchase is reused from the archive while fresh, so it buys at most
        once a week per competitor (once a day for mentions); it is capped by the
        client's monthly budget, and a failed or over-budget read falls back to the free
        signal. Quote it first with estimate_cost. Answers 'tell me when rankings drop'."""
        return self.call("create_alert_rule", _present({"clientId": client_id, "kind": kind, "threshold": threshold, "cooldownHours": cooldown_hours, "webhookUrl": webhook_url, "channel": channel, "emailRecipients": email_recipients, "telegramChatId": telegram_chat_id, "paidSource": paid_source}))

    def create_api_key(self, *, name: str, client_id: Optional[str] = None, role: Optional[Literal["client_viewer", "analyst", "manager", "site_admin", "admin"]] = None, expires_in_days: Optional[int] = None, max_cost_usd_per_call: Optional[float] = None, mode: Optional[Literal["live", "test"]] = None) -> Any:
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
        return self.call("create_api_key", _present({"name": name, "clientId": client_id, "role": role, "expiresInDays": expires_in_days, "maxCostUsdPerCall": max_cost_usd_per_call, "mode": mode}))

    def create_business_post(self, *, client_id: str, summary: str, location_id: Optional[str] = None, call_to_action: Optional[Dict[str, Any]] = None, dry_run: Optional[bool] = None) -> Any:
        """Publish a Google Business Profile post. Publishes an update post (topic
        STANDARD) on the client's own Google Business Profile listing through its
        connected Business Profile: summary (up to 1,500 characters) and an optional
        callToAction — BOOK, ORDER, SHOP, LEARN_MORE or SIGN_UP with a url, or CALL with
        none (it dials the listing's phone). dryRun: true publishes nothing and returns
        the exact localPosts body. The answer carries Google's name for the post and its
        state (PROCESSING until Google has reviewed it, LIVE, or REJECTED for its
        content policy). Refused with missing_scope or not_connected as
        update_business_profile is. get_business_posts reads the posts already there.
        Answers 'post this offer on our Google listing'. Free."""
        return self.call("create_business_post", _present({"clientId": client_id, "locationId": location_id, "summary": summary, "callToAction": call_to_action, "dryRun": dry_run}))

    def create_client(self, *, name: str, domain: str, keywords: Optional[List[str]] = None, monthly_budget_usd: Optional[float] = None) -> Any:
        """Create a client. Onboards a client in one step: the client, a project, its site
        and a rank tracker, optionally with keywords to track. Answers 'set up a new
        client'. Refused when the name is taken or the plan's client or keyword
        allowance is used up; every tracked keyword is a paid lookup on every run."""
        return self.call("create_client", _present({"name": name, "domain": domain, "keywords": keywords, "monthlyBudgetUsd": monthly_budget_usd}))

    def create_data_sync(self, *, client_id: str, destination: Literal["google_sheets", "airtable", "bigquery"], name: str, query: Dict[str, Any], mode: Optional[Literal["append", "replace"]] = None, window_days: Optional[int] = None, cadence: Optional[Literal["daily", "weekly", "monthly"]] = None, run_hour: Optional[int] = None, spreadsheet_id: Optional[str] = None, sheet: Optional[str] = None, base_id: Optional[str] = None, table: Optional[str] = None, project_id: Optional[str] = None, dataset_id: Optional[str] = None, table_id: Optional[str] = None) -> Any:
        """Sync data to a sheet, base or warehouse. Copies any dataset query (the
        query_data shape; see describe_datasets) to the client's Google Sheet
        (spreadsheetId, sheet), Airtable table (baseId, table — its fields named as the
        columns) or BigQuery table (projectId, datasetId, tableId — created on first
        run) on a schedule: daily, weekly or monthly at a UTC hour. replace swaps the
        contents each run; append adds rows, and with windowDays reads only the last N
        days ending yesterday so no day is added twice. Needs that destination connected
        first (get_integration_connect_link for Google, connect_integration for
        Airtable). Answers 'put our Search Console pages in a sheet every Monday', 'send
        the analytics to BigQuery daily'. Free."""
        return self.call("create_data_sync", _present({"clientId": client_id, "destination": destination, "name": name, "query": query, "mode": mode, "windowDays": window_days, "cadence": cadence, "runHour": run_hour, "spreadsheetId": spreadsheet_id, "sheet": sheet, "baseId": base_id, "table": table, "projectId": project_id, "datasetId": dataset_id, "tableId": table_id}))

    def create_deploy_hook(self, *, client_id: str, sitemap_url: Optional[str] = None) -> Any:
        """Create a deploy hook. Answers 'tell search engines whenever we deploy'. Makes
        the client's deploy hook: a secret URL the site's pipeline calls after every
        deploy (one curl, or a Netlify/Vercel/Cloudflare Pages/Coolify notification).
        Each call reads the sitemap, compares it with the last one, and submits the new
        and changed pages to IndexNow; the first call records the baseline only. Returns
        the URL once, with how to call it from each platform. Making it again replaces
        the URL. Free."""
        return self.call("create_deploy_hook", _present({"clientId": client_id, "sitemapUrl": sitemap_url}))

    def create_funnel(self, *, client_id: str, name: str, steps: List[Dict[str, Any]]) -> Any:
        """Define a funnel. Defines a funnel: 2 to 8 steps (a page reached or an event
        sent) a visit should pass through in order — landing page, product, cart,
        thank-you. Measured within one visit, because the cookieless visitor id resets
        daily. Answers 'how many who see pricing go on to sign up'. Free."""
        return self.call("create_funnel", _present({"clientId": client_id, "name": name, "steps": steps}))

    def create_goal(self, *, client_id: str, name: str, kind: Literal["pageview", "event"], match: str, value_minor: Optional[int] = None) -> Any:
        """Define a conversion goal. Defines a goal for the cookieless analytics: reaching
        a page (kind pageview, match a path such as /thanks or /signup/*) or sending a
        custom event (kind event, match its name). Optionally worth a fixed value in
        minor units (2500 = 25.00); without one, an event's own 'value' property is
        summed. Counts every visit since the tag went in, not only from now. Answers
        'count sign-ups as reaching /welcome'. Free."""
        return self.call("create_goal", _present({"clientId": client_id, "name": name, "kind": kind, "match": match, "valueMinor": value_minor}))

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
        the same words for another country are a different keyword. Each keyword may
        carry the metrics another tool already returned for it (volume, difficulty, CPC,
        intent, SERP features), stored with their read time so the list starts with
        numbers without buying them twice. Returns created: false with the reason when
        the name is already taken, rather than failing."""
        return self.call("create_keyword_list", _present({"name": name, "clientId": client_id, "keywords": keywords}))

    def create_lead_widget(self, *, name: str, heading: Optional[str] = None, accent_color: Optional[str] = None, allowed_origins: Optional[List[str]] = None, notify_emails: Optional[List[str]] = None) -> Any:
        """Create a lead-gen audit widget. Makes an audit form for the agency's own
        website: a visitor enters their URL and email, sees a short audit of the page on
        the spot, and lands in list_leads. Returns embedCode to paste into the site and
        frameUrl for the form alone. Answers 'put a free audit form on our site'.
        Limited per visitor and guarded against internal addresses. Free."""
        return self.call("create_lead_widget", _present({"name": name, "heading": heading, "accentColor": accent_color, "allowedOrigins": allowed_origins, "notifyEmails": notify_emails}))

    def create_outreach_sequence(self, *, client_id: str, name: str, steps: List[Dict[str, Any]]) -> Any:
        """Create an outreach sequence. Saves a sequence for the client: the first email
        and up to five follow-ups, each sent delayDays after the one before unless the
        prospect has replied (the first step's delay is ignored: it goes when
        send_outreach is called). Subjects and bodies may use {{site}} (the prospect's
        domain), {{page}} (its page, or the domain) and {{client}} (the client's name).
        Follow-ups go into the same thread. Answers 'set up a three-step outreach
        sequence'. Free."""
        return self.call("create_outreach_sequence", _present({"clientId": client_id, "name": name, "steps": steps}))

    def create_portal_link(self, *, client_id: str, label: str) -> Any:
        """Create a client portal link. Makes a white-label link that shows one client
        their own dashboard under the agency's name, with no sign-in. Answers 'give the
        client a link to their results'. The full address is in this response once and
        can never be shown again; send it to the client and keep it out of logs. Anyone
        holding it can see that client's results until it is revoked."""
        return self.call("create_portal_link", _present({"clientId": client_id, "label": label}))

    def create_portfolio(self, *, name: str, description: Optional[str] = None, members: Optional[List[Dict[str, Any]]] = None) -> Any:
        """Create a portfolio. Groups clients, or single sites of clients, under a name, to
        read their traffic, rankings, issues and AI visibility together with
        get_portfolio_metrics. Answers 'group the dental practices'. Names are unique in
        the agency. Every member must be a client the caller can reach."""
        return self.call("create_portfolio", _present({"name": name, "description": description, "members": members}))

    def create_project(self, *, client_id: str, name: str, domain: Optional[str] = None, location_code: Optional[int] = None, language_code: Optional[str] = None) -> Any:
        """Create a project. Adds a project to a client, optionally with a site domain to
        crawl. Answers 'add a second site or market for this client'. The domain is
        written like example.com."""
        return self.call("create_project", _present({"clientId": client_id, "name": name, "domain": domain, "locationCode": location_code, "languageCode": language_code}))

    def create_rank_tracker(self, *, client_id: str, name: str, project_id: Optional[str] = None, domain: Optional[str] = None, engine: Optional[Literal["google", "bing", "youtube", "amazon", "app_store", "yandex", "baidu", "naver", "duckduckgo", "yahoo", "seznam", "google_play"]] = None, device: Optional[Literal["desktop", "mobile", "both"]] = None, frequency: Optional[Literal["daily", "weekly", "monthly", "manual"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, run_hour: Optional[int] = None, run_day: Optional[int] = None, depth: Optional[int] = None, match: Optional[Literal["domain", "subdomains", "prefix"]] = None, url_prefix: Optional[str] = None) -> Any:
        """Create a rank tracker. Starts tracking a client's positions on one engine,
        device and locale. Answers 'track this client on Bing too' or 'track mobile
        separately'. Defaults to the client's first project and site domain. Engine and
        locale cannot be changed later — they are part of every keyword's identity — so
        a different market is a new tracker. A locale can be a city, county or region,
        not only a country: search_locations finds the code. Cadence daily, weekly,
        monthly or manual, at a chosen UTC hour and day; depth 10–200; match the exact
        host, its subdomains, or a URL prefix."""
        return self.call("create_rank_tracker", _present({"clientId": client_id, "name": name, "projectId": project_id, "domain": domain, "engine": engine, "device": device, "frequency": frequency, "locationCode": location_code, "languageCode": language_code, "runHour": run_hour, "runDay": run_day, "depth": depth, "match": match, "urlPrefix": url_prefix}))

    def create_report(self, *, client_id: str, title: str, sections: List[Literal["rank-summary", "share-of-voice", "keyword-movers", "backlink-summary", "traffic", "core-web-vitals", "site-health", "audit-summary"]]) -> Any:
        """Create a report. Saves a report for a client from a list of sections; each is
        wired to the client's own tracker and site. Answers 'build a monthly report for
        this client'. Sections the client has nothing for yet are left out. Send it with
        send_report; schedules are set in the app."""
        return self.call("create_report", _present({"clientId": client_id, "title": title, "sections": sections}))

    def create_report_link(self, *, client_id: str, report_id: str, expires_in_days: Optional[int] = None, period_days: Optional[int] = None) -> Any:
        """Make a shareable report page. A signed, expiring, read-only link to one of a
        client's saved reports (from list_reports) as a web page under the agency's own
        branding, plus downloadUrl for the same report as a self-contained HTML file.
        Answers 'send the client a link to the report' or 'give me the report as HTML'.
        Covers the last periodDays days (default 30) as of now, fixed: the page does not
        change as time passes. Anyone holding the link can read it until it expires
        (expiresInDays, default 14, at most 90), so only make one when the user asks.
        The url is shown only in this answer and is never stored; linkId names it for
        list_report_links and revoke_report_link. revoke_report_links turns every
        earlier link off. Free."""
        return self.call("create_report_link", _present({"clientId": client_id, "reportId": report_id, "expiresInDays": expires_in_days, "periodDays": period_days}))

    def create_task(self, *, client_id: str, title: str, notes: Optional[str] = None, status: Optional[Literal["todo", "in_progress", "done", "wont_do"]] = None, assignee_user_id: Optional[str] = None, due_date: Optional[str] = None, link: Optional[Dict[str, Any]] = None, crawl_id: Optional[str] = None) -> Any:
        """Add a task. Adds a task to a client's list, optionally assigned, dated and
        linked to an audit issue, a page or a keyword. Answers 'remind us to rewrite the
        pricing page by Friday'. One open task per audit issue: a second is refused
        while the first is open."""
        return self.call("create_task", _present({"clientId": client_id, "title": title, "notes": notes, "status": status, "assigneeUserId": assignee_user_id, "dueDate": due_date, "link": link, "crawlId": crawl_id}))

    def create_tasks_from_audit(self, *, client_id: str, crawl_id: Optional[str] = None, rule_ids: Optional[List[str]] = None, severities: Optional[List[Literal["critical", "warning", "notice"]]] = None, assignee_user_id: Optional[str] = None, due_date: Optional[str] = None, limit: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Turn audit issues into tasks. Makes one task per issue a crawl found — titled
        from the issue, with its page count and howToFix in the notes — for the chosen
        rule ids or every issue of the chosen severities (default critical and warning).
        Issues that already have an open task are skipped, so this is safe after every
        crawl. Findings accepted as intentional (accept_issue) are left out, and an
        issue they cover entirely makes no task. With path owners set (set_path_owners),
        each task names the owner of most of its pages, and its notes say how the pages
        split between owners. crawlId defaults to the latest completed crawl. dryRun:
        true makes nothing and lists wouldCreate (each task's title, notes, assignee and
        due date) and skipped. Answers 'put the audit on our to-do list'. Free."""
        return self.call("create_tasks_from_audit", _present({"clientId": client_id, "crawlId": crawl_id, "ruleIds": rule_ids, "severities": severities, "assigneeUserId": assignee_user_id, "dueDate": due_date, "limit": limit, "dryRun": dry_run}))

    def create_webhook(self, *, url: str, events: List[Literal["crawl.completed", "gsc.synced", "rank.moved", "backlink.new", "backlink.lost", "issue.new_critical", "ai.citation.gained", "ai.citation.lost", "competitor.page.new", "budget.threshold", "alert.fired"]], client_id: Optional[str] = None) -> Any:
        """Subscribe a URL to events. Sends events to an https URL as they happen, signed:
        each POST carries Seolyticize-Signature: t=<unix>,v1=<hex HMAC-SHA256 of
        "<t>.<body>" with the secret>, plus Seolyticize-Event and Seolyticize-Delivery
        headers. Retried with backoff (1 min to a day) until a 2xx; replay_webhooks
        sends missed ones again. Events: crawl.completed, gsc.synced, rank.moved,
        backlink.new, backlink.lost, issue.new_critical, ai.citation.gained,
        ai.citation.lost, competitor.page.new, budget.threshold, alert.fired. clientId
        limits it to one client; null is every client. The secret is in the response
        once. Answers 'tell my system when a crawl finishes'. Free."""
        return self.call("create_webhook", _present({"clientId": client_id, "url": url, "events": events}))

    def delete_alert_rule(self, *, client_id: str, rule_id: str) -> Any:
        """Delete an alert rule. Deletes a rule and every alert it ever fired. Answers
        'remove this alert for good'. To stop it but keep its history, pause it with
        update_alert_rule instead. Safe to repeat."""
        return self.call("delete_alert_rule", _present({"clientId": client_id, "ruleId": rule_id}))

    def delete_data_sync(self, *, client_id: str, sync_id: str) -> Any:
        """Delete a data sync. Stops and removes a sync. What it already wrote stays where
        it is. Answers 'stop the Airtable sync'. Safe to repeat."""
        return self.call("delete_data_sync", _present({"clientId": client_id, "syncId": sync_id}))

    def delete_digest_schedule(self, *, client_id: str, digest_id: str) -> Any:
        """Stop a digest. Stops posting the weekly digest to that chat. Answers 'stop the
        Monday Slack digest'. Safe to repeat."""
        return self.call("delete_digest_schedule", _present({"clientId": client_id, "digestId": digest_id}))

    def delete_funnel(self, *, client_id: str, funnel_id: str) -> Any:
        """Delete a funnel. Deletes a funnel definition. Answers 'remove that funnel'. Safe
        to repeat."""
        return self.call("delete_funnel", _present({"clientId": client_id, "funnelId": funnel_id}))

    def delete_goal(self, *, client_id: str, goal_id: str) -> Any:
        """Delete a goal. Deletes a goal. The events it counted are untouched. Answers
        'stop counting that goal'. Safe to repeat."""
        return self.call("delete_goal", _present({"clientId": client_id, "goalId": goal_id}))

    def delete_keyword_list(self, *, list_id: str) -> Any:
        """Delete a keyword list. Deletes a keyword list and the keywords on it, for good.
        Answers 'get rid of that list'. Keywords a tracker took from the list stay
        tracked."""
        return self.call("delete_keyword_list", _present({"listId": list_id}))

    def delete_portfolio(self, *, portfolio_id: str) -> Any:
        """Delete a portfolio. Deletes a portfolio; its clients and sites are untouched.
        Needs access to every client in it. Answers 'drop that portfolio'."""
        return self.call("delete_portfolio", _present({"portfolioId": portfolio_id}))

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

    def delete_task(self, *, client_id: str, task_id: str) -> Any:
        """Delete a task. Deletes a task outright. Prefer update_task with status wont_do,
        which keeps the record. Answers 'remove that task'. Safe to repeat."""
        return self.call("delete_task", _present({"clientId": client_id, "taskId": task_id}))

    def delete_webhook(self, *, webhook_id: str) -> Any:
        """Delete a webhook. Stops a webhook for good, with its queued deliveries. Answers
        'stop sending to that URL'. Free."""
        return self.call("delete_webhook", _present({"webhookId": webhook_id}))

    def delete_written_report(self, *, client_id: str, report_id: str) -> Any:
        """Delete a written report. Permanently deletes one written report; its share link
        stops working at once. Answers 'remove that report'. Does not touch data
        reports, templates or anything else. Free."""
        return self.call("delete_written_report", _present({"clientId": client_id, "reportId": report_id}))

    def describe_datasets(self) -> Any:
        """What can be queried. The datasets query_data and export_data read — Search
        Console (every day kept), cookieless analytics events, crawl pages, issues and
        links, rank captures, backlinks, imported revenue (orders with their channel and
        landing page), AI assistant visits — with their columns, metrics, time column
        and how long each is kept. Answers 'what data is there to ask about'. Free."""
        return self.call("describe_datasets", {})

    def disconnect_app(self, *, grant_id: str) -> Any:
        """Disconnect an app. Stops a signed-in app working, at once: its access and
        refresh tokens both end. Answers 'remove that assistant's access'. Takes the
        grantId from list_connected_apps. The app can only come back if somebody signs
        in and approves it again. Safe to repeat."""
        return self.call("disconnect_app", _present({"grantId": grant_id}))

    def disconnect_integration(self, *, client_id: str, provider: Literal["stripe", "shopify", "paddle", "google_sheets", "bigquery", "airtable", "slack", "discord", "telegram", "jira", "linear", "github", "matomo"]) -> Any:
        """Disconnect a tool. Removes a connection and its sealed key, with the syncs,
        digests and task links that ran through it. Revoke the key at the provider too.
        Answers 'disconnect their Stripe'. Safe to repeat."""
        return self.call("disconnect_integration", _present({"clientId": client_id, "provider": provider}))

    def draft_agent_files(self, *, client_id: str, ai_train: Literal["yes", "no"], ai_input: Optional[Literal["yes", "no"]] = None, search: Optional[Literal["yes", "no"]] = None, urls: Optional[List[str]] = None) -> Any:
        """Draft the site's files for AI agents. Drafts, for the client's site, the files
        AI agents read — nothing is published: robots.txt with a Content-Signal line
        (search, ai-input, ai-train) in every user-agent group, every Allow and Disallow
        kept exactly as it is, with aiTrain the user's own choice; an ai-catalog.json in
        the Agentic Resource Discovery 1.0 shape (specVersion 1.0, standard media types
        and placeholder representativeQueries) listing the agent card the site already
        has, with resources ARD has no type for (llms.txt, sitemaps, API catalogs) named
        in skipped; and WebMCP tool stubs (document.modelContext, falling back to
        navigator.modelContext) carrying readOnlyHint, consequentialHint and
        untrustedContentHint, one per real form found on the homepage and the pages
        given or its contact, booking and sign-up pages, with forms that send, buy or
        delete marked consequential. Answers 'write our Content-Signal lines', 'make us
        an ai-catalog.json' and 'how do we expose our forms to browser agents'. Free."""
        return self.call("draft_agent_files", _present({"clientId": client_id, "aiTrain": ai_train, "aiInput": ai_input, "search": search, "urls": urls}))

    def draft_article(self, *, client_id: str, keyword: str, related_keywords: Optional[List[str]] = None, word_count: Optional[int] = None, instructions: Optional[str] = None, target_url: Optional[str] = None, depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Draft an article from the brief. Writes a full article draft for a keyword,
        grounded in the content brief built from the pages that rank: the intent and
        format that win, the target length, the outline, the must-cover terms and the
        questions to answer, in the client's voice from its brief. Returns Markdown with
        H2/H3 headings, a meta title and description with pixel-length checks, and which
        must-cover terms the draft uses and misses (checked by us, not claimed). When
        the keyword registry already gives the keyword to another page, ownership warns
        'this already belongs to /x' (targetUrl: the owner, to draft its rewrite
        instead). Answers 'write me a first draft for this keyword'. A paid Claude call
        on the client's budget, plus the brief's results page (free when anyone bought
        it in the last day). Run score_content on the result before publishing. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("draft_article", _present({"clientId": client_id, "keyword": keyword, "relatedKeywords": related_keywords, "wordCount": word_count, "instructions": instructions, "targetUrl": target_url, "depth": depth, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def draft_client_brief(self, *, client_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
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
        return self.call("draft_client_brief", _present({"clientId": client_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def draft_outreach_emails(self, *, client_id: str, prospect_ids: List[str], offer: str, our_url: Optional[str] = None, sender: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Draft outreach emails to link prospects. Drafts one short, personal pitch per
        prospect on the client's outreach list (up to 20): it names why this site was
        chosen — the dead page it links to, the thread, the article, the rivals it links
        to (from the prospect's reason and page) — and what is offered in its place
        (offer, and ourUrl when given), in the client's voice from its brief. Plain text
        with a subject; no templates stuffed with merge fields, no false flattery,
        nothing claimed that the prospect data does not show. Nothing is sent: copy them
        into your mail tool, then move the prospect to contacted with
        set_link_prospect_status. Answers 'write the outreach for these sites'. A
        metered Claude call on the client's budget; quote it with estimate_cost. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("draft_outreach_emails", _present({"clientId": client_id, "prospectIds": prospect_ids, "offer": offer, "ourUrl": our_url, "sender": sender, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def draft_review_replies(self, *, client_id: str, location_id: str, limit: Optional[int] = None, voice: Optional[str] = None, include_answered: Optional[bool] = None, trade: Optional[Literal["auto", "healthcare", "legal", "general"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Draft replies to a location's reviews. Drafts owner replies to a location's
        Google reviews that have no reply yet (newest first, up to limit): thanks that
        name what the reviewer praised, and for a poor review an apology, what will
        change and an offline route — never arguing, never inventing facts, no keyword
        stuffing. voice sets the tone in a sentence. trade (detected from the business
        by default) holds a healthcare practice's replies to patient privacy (HIPAA:
        never confirm the reviewer is a patient, never mention care) and a legal
        practice's to client confidentiality, and each draft that still slips carries a
        caution. Nothing is posted: read them, then post_review_reply. canPost says
        whether the listing is connected so they can be posted from here. Answers 'reply
        to our reviews'. A metered Claude call on the client's budget; quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("draft_review_replies", _present({"clientId": client_id, "locationId": location_id, "limit": limit, "voice": voice, "includeAnswered": include_answered, "trade": trade, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def draft_seo_strategy(self, *, client_id: str, competitors: Optional[List[str]] = None, instructions: Optional[str] = None, save: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Draft an SEO strategy. Drafts a 12-month SEO strategy for the client and saves
        it as a written report (save: false returns it without saving): a plan for its
        business type (SaaS, local, ecommerce, publisher or agency, as get_seo_scorecard
        detects it) in four phases — weeks 1–4, weeks 5–12, weeks 13–24 and months 7–12
        — a teardown of the top five competitors (competitors, else the brief's and the
        ones we see ranking beside it) from the data we hold, a KPI table at baseline,
        3, 6 and 12 months with baselines from Search Console and targets from
        forecast_search_clicks, plus indexed pages (URL Inspection, against the pages
        meant to be indexed) and phone Core Web Vitals (Chrome UX Report p75 against
        Google's good lines), the site structure from the latest crawl, the URL
        architecture and a schema plan by page type for the business type (no FAQPage,
        no self-serving ratings), and a calendar from plan_content (the stored plan, or
        a new one built when there is none). Every figure comes from the client's data
        and is named with its source; Claude writes the prose around them and invents
        none. instructions adds the agency's own direction. One metered Claude call:
        quote it with estimate_cost. Answers 'write us an SEO strategy' and 'what is the
        plan for this client this year'. Can spend: pass max_cost_micros to cap it."""
        return self.call("draft_seo_strategy", _present({"clientId": client_id, "competitors": competitors, "instructions": instructions, "save": save, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

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

    def estimate_domain_traffic(self, *, client_id: str, targets: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Estimate search traffic for domains. A vendor's current estimate of monthly
        organic search traffic and ranking keywords for up to 100 domains, bought now.
        get_batch_analysis gives the same traffic beside rank, backlinks and referring
        domains for up to 200. Answers 'how much search traffic do these competitors
        get'. Modelled from rankings, not measured visits. batch_domain_metrics reads
        what is already stored for free; use this when those figures are missing or
        stale. A paid lookup on the client's account: quote it with estimate_cost. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("estimate_domain_traffic", _present({"clientId": client_id, "targets": targets, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def explain_keyword_difficulty(self, *, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, keyword_id: Optional[str] = None) -> Any:
        """Why a keyword is as hard as it is. Which first-page results set a keyword's
        difficulty score and which make it harder than the score suggests: each result's
        referring domains and role (sets the median, above it, below it, or unscored for
        lack of link data), the strongest and weakest result, the domain authority
        beside each, and a one-paragraph summary. Answers 'why is this keyword a 47' so
        the number can be checked rather than trusted. Read from the archive and our
        link graph; buys nothing, and a keyword never captured is reported unscored."""
        return self.call("explain_keyword_difficulty", _present({"term": term, "locationCode": location_code, "languageCode": language_code, "keywordId": keyword_id}))

    def explain_result(self, *, client_id: str, tool: str, result: Any, audience: Optional[Literal["client", "team"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Explain a result in plain words. Reads any earlier tool result (pass the tool's
        name and its data) and says, in plain language for a client or for the team,
        what it shows, what matters in it and what to do next — for handing off to
        people who don't read JSON. Answers 'what does this mean for the client'. A
        metered Claude call on the client's budget; quote it with estimate_cost. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("explain_result", _present({"clientId": client_id, "tool": tool, "result": result, "audience": audience, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def explore_ai_prompt(self, *, prompt: str, client_id: Optional[str] = None, engines: Optional[List[Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"]]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Ask assistants one question now. Asks one question live on the chosen assistants
        (claude, and any the agency has its own API key for) and returns each answer's
        text, citations, and — when clientId is given — which tracked brands it named.
        Nothing is stored; use it to see what assistants say before tracking a question,
        or to look up how they describe a brand. Answers 'what does ChatGPT say about
        this'. Claude is metered (meteredMicros); others bill the agency's own accounts.
        Can spend: pass max_cost_micros to cap it."""
        return self.call("explore_ai_prompt", _present({"clientId": client_id, "prompt": prompt, "engines": engines, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def export_ai_visibility_data(self, *, client_id: str, days: Optional[int] = None, include: Optional[Literal["mentions", "answers"]] = None) -> Any:
        """Export AI visibility data. CSV of the last N days (default 90): include
        "mentions" for one row per answer and brand (named, position, cited), or
        "answers" for the full answer text and citations (up to 2,000 answers). Returns
        rows and csv. Answers 'give me the raw data for a deck'. Free."""
        return self.call("export_ai_visibility_data", _present({"clientId": client_id, "days": days, "include": include}))

    def export_data(self, *, client_id: str, dataset: Literal["gsc", "web_events", "crawl_pages", "crawl_issues", "crawl_links", "rank_captures", "backlinks", "revenue_orders", "web_agent_visits"], dimensions: Optional[List[str]] = None, metrics: Optional[List[str]] = None, columns: Optional[List[str]] = None, filters: Optional[List[Dict[str, Any]]] = None, from_: Optional[str] = None, to: Optional[str] = None, order_by: Optional[List[Dict[str, Any]]] = None, crawl_id: Optional[str] = None, limit: Optional[int] = None, format_: Optional[Literal["csv", "jsonl", "parquet"]] = None) -> Any:
        """Export stored data to a file. The same query as query_data, written to a file —
        CSV, JSON lines or Parquet, up to a million rows — with a download link valid
        for 24 hours, for BigQuery, a notebook or a spreadsheet. Answers 'give me all of
        our Search Console history' and 'export the crawl'. Free."""
        return self.call("export_data", _present({"clientId": client_id, "dataset": dataset, "dimensions": dimensions, "metrics": metrics, "columns": columns, "filters": filters, "from": from_, "to": to, "orderBy": order_by, "crawlId": crawl_id, "limit": limit, "format": format_}))

    def export_search_console_data(self, *, client_id: str, from_: str, to: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, country: Optional[str] = None, device: Optional[Literal["DESKTOP", "MOBILE", "TABLET"]] = None, dimension: Optional[Literal["query", "page"]] = None) -> Any:
        """Export Search Console queries or pages as CSV. Google Search Console queries or
        pages (dimension) for a search type, date range, and optionally one country and
        device, as CSV with clicks, impressions, click-through rate and average position
        — up to 5,000 rows. Returns filename, rows and csv. Cells a spreadsheet would
        run as formulas are neutralised. Answers 'give me the query data in a
        spreadsheet'. Free."""
        return self.call("export_search_console_data", _present({"clientId": client_id, "searchType": search_type, "from": from_, "to": to, "country": country, "device": device, "dimension": dimension}))

    def export_sitemap(self, *, client_id: str) -> Any:
        """Write the sitemap from the latest audit. Writes sitemap.xml from the client's
        latest complete crawl: every 200 HTML page that is indexable and canonical to
        itself, deduplicated and sorted, with no lastmod (the crawl knows when it read a
        page, not when it changed). Past 50,000 URLs or 50 MB a file, it splits into
        sitemap-1.xml, sitemap-2.xml… under a sitemap.xml index whose locations assume
        the parts sit at the site's root. Returns a download link per file, valid for a
        day. Answers 'make us a clean sitemap' and 'what should our sitemap list'. Free."""
        return self.call("export_sitemap", _present({"clientId": client_id}))

    def find_journalist_requests(self, *, client_id: str, feeds: Optional[List[str]] = None, keywords: Optional[List[str]] = None, days: Optional[int] = None, limit: Optional[int] = None, add_to_list: Optional[bool] = None) -> Any:
        """Journalist requests for sources, from feeds. Reads RSS or Atom feeds of
        journalist requests for sources and keeps those matching the keywords (all of
        them when none are given), newest first, with the deadline where the request
        states one. With no feeds given it reads the public #journorequest,
        #journorequests and #prrequest feeds on Mastodon (mastodon.social and
        journa.host) and says so in defaultFeeds, so keywords alone work. Source of
        Sources sends its queries by email only, Qwoted's and Featured's requests need
        an account, and SourceBottle publishes no feed — for those, give an email-to-RSS
        address subscribed to one, or any niche request board's feed. addToList puts
        each request with a site of its own on the outreach list (needs client:manage);
        social posts have none. Answers 'which journalists want a source on our topic
        this week'. Free."""
        return self.call("find_journalist_requests", _present({"clientId": client_id, "feeds": feeds, "keywords": keywords, "days": days, "limit": limit, "addToList": add_to_list}))

    def find_link_opportunities(self, *, client_id: str, topic: str, kinds: Optional[List[Literal["resource_pages", "best_lists", "roundups", "podcasts", "newsletters"]]] = None, queries_per_kind: Optional[int] = None, depth: Optional[int] = None, exclude_domains: Optional[List[str]] = None, add_to_list: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Resource pages, best-of lists, roundups, podcasts and newsletters for a topic.
        Finds places that link out by design, from Google results for the search
        footprints link builders use: resource pages ("useful links",
        intitle:resources), "best X" lists, link roundups, podcasts inviting guests, and
        newsletters taking sponsors or guest pieces — each with the query that found it,
        its title, snippet and position. The client's own domain and the giant platforms
        are left out. addToList puts every page on the client's outreach list (as
        add_link_prospects would; needs client:manage). Answers 'which resource pages
        could list us', 'which podcasts take guests in our niche' and 'where can we
        sponsor a newsletter'. One results page per query: queriesPerKind × kinds reads.
        A paid lookup on the client's account unless anyone read the same thing recently
        (spend says which); quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("find_link_opportunities", _present({"clientId": client_id, "topic": topic, "kinds": kinds, "queriesPerKind": queries_per_kind, "depth": depth, "excludeDomains": exclude_domains, "addToList": add_to_list, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def find_serp_competitors(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, limit: Optional[int] = None, exclude: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who competes across a keyword set. Finds the domains that rank across a set of
        keywords (up to 200) in one market: visibility (share of the keywords they hold
        in the top ten), keyword count, average position and estimated traffic. Answers
        'who are our real search competitors for these terms'. List the client's own
        domain in exclude. One purchase per call. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("find_serp_competitors", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "limit": limit, "exclude": exclude, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def find_tools(self, *, task: str, limit: Optional[int] = None) -> Any:
        """Find the tools for a task. Given a task in plain words ('why did traffic drop',
        'write an article about X', 'who links to my rivals'), returns the 5–10 tools
        for it, best first, each with what it does and whether it costs money — and the
        named recipe that covers the task, when one does. Use it instead of reading the
        whole catalogue. Answers 'which tool do I use for this'. Free."""
        return self.call("find_tools", _present({"task": task, "limit": limit}))

    def find_unlinked_mentions(self, *, client_id: str, brand: Optional[str] = None, since: Optional[str] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Pages that name the brand but don't link to it. Finds pages that mention the
        client's brand (brand, or the brand terms from its brief) from DataForSEO's
        content index, one per site, then reads each (up to limit) and keeps those with
        no link to the client's site — the easiest links to win, since the writer
        already chose to talk about it. Each with its domain rank, date and the sentence
        that names the brand. Answers 'who mentions us without linking'. A paid
        DataForSEO read plus free page reads; quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("find_unlinked_mentions", _present({"clientId": client_id, "brand": brand, "since": since, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def forecast_keyword_traffic(self, *, client_id: str, keywords: List[Dict[str, Any]], positions: Optional[List[int]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None) -> Any:
        """What a keyword set is worth at target positions. Estimated organic clicks for a
        set of keywords at the positions aimed for (default 1, 3, 5 and 10): volume ×
        the click curve for the market (measured by the panel where it can be, published
        otherwise, and said which), shaped month by month by each keyword's seasonality
        from stored monthly volumes, with a time-to-rank estimate from difficulty and
        the client's current position, and first-year clicks counting only from the
        month the page is likely to arrive. Totals for the set. keywords are strings, or
        { term, searchVolume, difficulty } when the figures are known. Answers 'what is
        this cluster worth if we rank'. Free: volumes and difficulty are read from what
        is stored, or given; a keyword never looked up is reported with unknown volume
        rather than zero."""
        return self.call("forecast_keyword_traffic", _present({"clientId": client_id, "keywords": keywords, "positions": positions, "locationCode": location_code, "languageCode": language_code}))

    def forecast_search_clicks(self, *, client_id: str, horizon_days: Optional[int] = None, trends: Optional[List[Dict[str, Any]]] = None, scenario: Optional[bool] = None) -> Any:
        """The next 90 days of non-branded clicks. Forecasts daily non-branded Google
        clicks for the next 90 days (horizonDays) from the site's own history: level, a
        damped trend, the weekly rhythm and last year's seasonality (needs 13 months of
        history; with less, pass trends — Google Trends interest for the site's head
        term from get_google_trends, past_5_years — to stand in), with an 80% band.
        scenario adds 'what if we win the striking-distance set': every query at
        positions 4–15 moved to 3, using the site's own click-through curve, the gain
        arriving over 60 days. Answers 'how much traffic should we expect next quarter'
        and 'what is the striking-distance work worth'. Free."""
        return self.call("forecast_search_clicks", _present({"clientId": client_id, "horizonDays": horizon_days, "trends": trends, "scenario": scenario}))

    def generate_hreflang(self, *, client_id: str, crawl_id: Optional[str] = None, x_default: Optional[str] = None, method: Optional[Literal["auto", "html", "http", "sitemap"]] = None, limit: Optional[int] = None) -> Any:
        """Write the hreflang for the site. Generates hreflang for every group of language
        versions in a crawl (tied by existing hreflang, or the same path under a
        language prefix such as /es/ or /de-at/), each with a self-reference and an
        x-default (xDefault names the fallback language; default the language of the
        unprefixed pages): <link> tags for groups under 50 versions, a Link HTTP header
        for PDFs, and an xhtml:link sitemap for groups of 50 or more (method forces
        one). Lists groups with two pages claiming one language, and pages whose
        language could not be told. Answers 'write our hreflang tags' and 'give me an
        hreflang sitemap'. Free."""
        return self.call("generate_hreflang", _present({"clientId": client_id, "crawlId": crawl_id, "xDefault": x_default, "method": method, "limit": limit}))

    def generate_llms_txt(self, *, client_id: str, max_links: Optional[int] = None, summary: Optional[str] = None) -> Any:
        """Write the site's llms.txt. Builds an llms.txt for the client's site (the
        llmstxt.org format: a title, a one-line summary, then sections of links with a
        description each) from its latest complete crawl — the pages meant to rank,
        strongest by internal PageRank, grouped by section, each with its own title and
        description. Says whether the site already publishes one and whether it differs.
        Nothing is published: put the markdown at publishAt. Answers 'make us an
        llms.txt'. Free."""
        return self.call("generate_llms_txt", _present({"clientId": client_id, "maxLinks": max_links, "summary": summary}))

    def generate_schema(self, *, client_id: str, url: str, type_: Optional[Literal["Product", "ProductGroup", "Article", "FAQPage", "HowTo", "SoftwareApplication", "Service", "Organization", "LocalBusiness", "VideoObject", "ProfilePage", "QAPage", "DiscussionForumPosting", "ItemList", "SoftwareSourceCode"]] = None, local_business_type: Optional[str] = None, opening_hours: Optional[List[Dict[str, Any]]] = None, area_served: Optional[List[str]] = None, shipping: Optional[Dict[str, Any]] = None, returns: Optional[Dict[str, Any]] = None) -> Any:
        """Write a page's structured data. Reads one page of the client's site and writes
        the JSON-LD it should carry: a BreadcrumbList from its path; on the homepage an
        Organization (with an @id, the social profiles the page itself links to, and the
        logo from its Open Graph image) and a WebSite; a LocalBusiness from the client's
        saved location, as the subtype its vertical calls for (from the page's words, or
        localBusinessType; never the deprecated Attorney), with the address split into a
        PostalAddress, an @id, branchOf when the client has several locations,
        openingHoursSpecification from openingHours, areaServed for a service-area
        business, and never a self-serving aggregateRating; an Article for a post, with
        dates and author only where the page states them. Nothing is invented — a field
        the page does not state is left out and named in notes — and types the page
        already has are listed. Also Product (price, currency, availability and brand
        from the page's product tags, with OfferShippingDetails and MerchantReturnPolicy
        from shipping and returns), VideoObject for an embedded YouTube or Vimeo video
        (Clip per chapter the page lists, else SeekToAction; BroadcastEvent for a live
        stream), ProfilePage on an author or team page, QAPage on a question page,
        DiscussionForumPosting on a forum thread, an ItemList of a hub's own pages,
        SoftwareSourceCode for a page linking its repository, HowTo (its ordered list of
        steps; Google retired the rich result), Service (for /services/ pages), and on
        request (type) ProductGroup, FAQPage, SoftwareApplication, Organization,
        LocalBusiness or Article on any page. Every block is checked against Google's
        required and recommended properties for its type (validation), so it is clear
        whether it can earn a rich result as written. FAQPage is written only when asked
        for: Google stopped showing FAQ rich results for every site on 7 May 2026, and
        any benefit with assistants is unconfirmed; FAQPage and HowTo blocks carry
        richResultEligible: false with the reason. Answers 'what schema should this page
        have', 'write product schema for this page' and 'mark up our locations'. Free."""
        return self.call("generate_schema", _present({"clientId": client_id, "url": url, "type": type_, "localBusinessType": local_business_type, "openingHours": opening_hours, "areaServed": area_served, "shipping": shipping, "returns": returns}))

    def get_agent_readiness(self, *, client_id: str, render: Optional[bool] = None) -> Any:
        """Get agent readiness. Whether the client's site can be read, cited and used by AI
        assistants and browsing agents. The original findings (crawler access,
        rendering, structured data, speed) plus prioritised checks: P0 a made-up path
        returns a real 404, CLS ≤ 0.1 (Chrome UX Report), robots.txt answers (a 5xx
        fails), and the homepage's primary content is there without JavaScript (under 50
        words in an app shell fails, under 150 warns); P1 a Content-Signal line in every
        robots.txt group with valid syntax (search, ai-input, ai-train, each yes or no),
        llms.txt as Lighthouse checks it (an H1, a Markdown link, 50+ characters; a
        catch-all HTML page fails; /llms-full.txt reported), Markdown delivery (a .md
        twin, or Accept: text/markdown answered with Vary: Accept), no /.well-known path
        answering 200 with HTML, and no WebMCP tool telling the agent to skip the user's
        confirmation; P2 /.well-known/api-catalog and OAuth metadata where the site runs
        APIs, WebMCP tools registered with document.modelContext (navigator.modelContext
        alone warns), and an accessibility-tree heuristic (0–100: accessible names,
        valid roles, nothing focusable hidden) from the rendered homepage; P3
        ai-catalog.json found in Lighthouse's order (robots.txt Agentmap, <link
        rel=ai-catalog>, Link header, /.well-known/ai-catalog.json) and validated
        against the ARD 1.0 rules (P1 when a signalled catalog fails or errors),
        agent-card.json, /.well-known/ucp for stores validated against the UCP shape,
        and declarative WebMCP form attributes. Each check is pass, fail, warn,
        unmeasured or not applicable; no fix below P0 is recommended while a measured P0
        fails. Answers 'why are assistants not citing us' and 'is our site ready for AI
        agents'. Free."""
        return self.call("get_agent_readiness", _present({"clientId": client_id, "render": render}))

    def get_ai_agent_visits(self, *, client_id: str, by: Optional[Literal["agent", "operator", "page", "day"]] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """AI assistants reading the site. How often AI assistants read the client's pages
        on somebody's behalf — ChatGPT-User, ChatGPT's agent mode, Claude-User,
        Perplexity-User, Mistral — by assistant, operator, page or day, seen by the tag
        or a server-side collector and kept apart from visits by people. Answers 'which
        pages is ChatGPT reading' and 'are assistants citing us more'. Training and
        index crawlers are not here: analyse_server_log reads those from the logs. Free."""
        return self.call("get_ai_agent_visits", _present({"clientId": client_id, "by": by, "days": days, "limit": limit}))

    def get_ai_answer_share(self, *, client_id: str, weeks: Optional[int] = None, engine: Optional[str] = None) -> Any:
        """Share of AI answers per topic, week by week. For each topic of the tracked
        questions, week by week across assistants (or one): how many answers there were,
        how many mentioned or cited the client, its share of answers, and its share of
        every tracked brand's mentions in them (share of voice). Answers 'are we winning
        the pricing questions in ChatGPT' and 'is our AI share growing by topic'. Free."""
        return self.call("get_ai_answer_share", _present({"clientId": client_id, "weeks": weeks, "engine": engine}))

    def get_ai_brand_mentions(self, *, client_id: str, brands: List[Dict[str, Any]], platform: Optional[Literal["google", "chat_gpt", "claude", "gemini", "perplexity", "copilot", "grok", "meta_ai", "deepseek", "ai_mode"]] = None, include_sampled: Optional[bool] = None, sampled_days: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Brand share of voice in AI answers. How often AI answers (Google AI Overviews,
        or ChatGPT) mention or cite each brand — the client and up to 9 competitors,
        each given as domains and/or brand keywords — across DataForSEO's database of
        real AI answers, with share of voice, the AI search volume behind the mentions,
        and the domains cited. No question tracking needed; works for any brand. Answers
        'what is our share of voice in AI search' and 'who do AI answers recommend'.
        Rows carry source: dataforseo (real users' prompts, with AI search volume) or
        sampled (the client's tracked questions asked by Seolyticize, no volume); the
        two are never summed. For platforms other than google and chat_gpt only sampled
        rows exist and the call is free. A paid lookup on the client's account unless
        anyone read the same thing recently (spend says which); quote it with
        estimate_cost. (about $0.10 a call) Can spend: pass max_cost_micros to cap it."""
        return self.call("get_ai_brand_mentions", _present({"clientId": client_id, "brands": brands, "platform": platform, "includeSampled": include_sampled, "sampledDays": sampled_days, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_citation_gap(self, *, client_id: str, our_url: str, prompt_id: Optional[str] = None, question: Optional[str] = None, cited_urls: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Why assistants cite others and not this page. For a question assistants answer
        without citing the client: reads the pages they did cite and the client's page
        (ourUrl), and says what the cited pages cover that the client's does not — the
        terms, the sections, the questions they answer — with a 0–100 coverage score and
        the fixes, as content scoring does against search results. The cited pages come
        from a tracked question's stored answers (promptId, free), from citedUrls
        (free), or by asking the ChatGPT app and Perplexity now (question, paid).
        Answers 'why does ChatGPT cite them and not us' and 'what should this page add
        to be cited'. Quote a live question with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_ai_citation_gap", _present({"clientId": client_id, "ourUrl": our_url, "promptId": prompt_id, "question": question, "citedUrls": cited_urls, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_citation_history(self, *, client_id: str, days: Optional[int] = None, engine: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Which of our pages assistants cite, over time. The client's pages cited in the
        tracked questions' AI answers over the last N days: per page, how many answers
        cited it, by which assistants, for which questions, first and last seen, and
        citations per week — and, per question and assistant, the pages gained and lost
        between its last two checks. Answers 'which pages does ChatGPT cite', 'did we
        lose a citation this week' and 'which content earns AI citations'. Free."""
        return self.call("get_ai_citation_history", _present({"clientId": client_id, "days": days, "engine": engine, "limit": limit}))

    def get_ai_cited_sources(self, *, client_id: str, days: Optional[int] = None, engine: Optional[Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"]] = None, limit: Optional[int] = None, topic: Optional[str] = None, segment: Optional[Literal["branded", "neutral"]] = None) -> Any:
        """Who owns the pages AI answers cite. The pages assistants cited for the client's
        tracked questions over the last N days (default 30), each domain classed by
        owner — own (the client's site), competitor (a tracked competitor's site,
        named), ugc (Reddit, Quora, YouTube, forums, social) or third_party (everyone
        else) — with each class's share of citations, each competitor's share, and the
        domains in order with their page type, questions, assistants and most-cited
        page. Counted once per answer. Filter by topic, segment or one assistant.
        Answers 'whose content are AI answers built from' and 'where should we get
        mentioned'. Free."""
        return self.call("get_ai_cited_sources", _present({"clientId": client_id, "days": days, "engine": engine, "limit": limit, "topic": topic, "segment": segment}))

    def get_ai_crawler_access(self, *, client_id: str, pages: Optional[int] = None, log: Optional[str] = None) -> Any:
        """Can each AI crawler reach and read the pages that matter. Per AI agent — GPTBot,
        OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User,
        PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended,
        Meta-ExternalAgent, CCBot — for the client's top pages by Search Console clicks:
        which robots.txt allows and blocks, whether the server or CDN turns it away when
        the homepage is fetched under its name, which pages need JavaScript to show
        their content (from the crawl's rendering, which AI crawlers do not do), and,
        given an access log, how often it came, how many pages it read and how many
        requests failed. A verdict (open, partial, blocked) and fixes per agent, its
        purpose (training, search, user) said. Answers 'can ChatGPT read our site' and
        'are we blocking AI search by accident'. Free."""
        return self.call("get_ai_crawler_access", _present({"clientId": client_id, "pages": pages, "log": log}))

    def get_ai_crawler_activity(self, *, client_id: str, days: Optional[int] = None) -> Any:
        """What AI crawlers read. From the client's connected logs: which pages GPTBot,
        ClaudeBot, PerplexityBot and every other AI agent fetched and how often — split
        by purpose (training crawls, search indexing, and fetches made for a user right
        now, the nearest a log gets to a citation) — with verified counts, error shares
        and when each was last seen. Google-Extended is a robots.txt opt-out token that
        Googlebot reads, not a crawler, so its robots.txt status is reported instead.
        Answers 'is ChatGPT reading our site', 'which pages does Perplexity fetch' and
        'are AI crawlers hitting errors'. Free."""
        return self.call("get_ai_crawler_activity", _present({"clientId": client_id, "days": days}))

    def get_ai_mode_answer(self, *, client_id: str, keyword: str, device: Optional[Literal["desktop", "mobile"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Google AI Mode for a keyword. What Google's AI Mode answers for a keyword, with
        every source it cites and whether the client is among them. Answers 'are we
        cited in AI Mode' and 'who does AI Mode trust for this'. A paid lookup on the
        client's account unless anyone read the same thing recently (spend says which);
        quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_ai_mode_answer", _present({"clientId": client_id, "keyword": keyword, "device": device, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_overview_citations(self, *, client_id: str, tracker_id: Optional[str] = None, feature: Optional[Literal["ai_overview", "featured_snippet", "people_also_ask"]] = None, days: Optional[int] = None) -> Any:
        """Who the AI Overview cites. For each tracked keyword: how often Google showed an
        AI Overview (or a featured snippet, or People Also Ask — feature), whether the
        client is cited, who is, and how that changed; plus the domains cited most
        across the keywords — the outreach and content targets. Answers 'are we in the
        AI Overview' and 'who does Google trust on this topic'. From the results pages
        already captured; free."""
        return self.call("get_ai_overview_citations", _present({"clientId": client_id, "trackerId": tracker_id, "feature": feature, "days": days}))

    def get_ai_prompt_research(self, *, client_id: str, keyword: str, platform: Optional[Literal["google", "chat_gpt", "claude", "gemini", "perplexity", "copilot", "grok", "meta_ai", "deepseek", "ai_mode"]] = None, limit: Optional[int] = None, include_sampled: Optional[bool] = None, sampled_days: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Real questions people ask AI about a topic. Questions real people put to AI
        assistants that contain a keyword, from DataForSEO's database of AI answers:
        each with its AI search volume, an excerpt of the answer, the sources cited, the
        brands named, the follow-up searches the assistant ran (fan-out), and whether
        the client is cited. Answers 'what do people ask ChatGPT about this' and 'which
        prompts should we track'. Rows carry source: dataforseo (real users' prompts,
        with AI search volume) or sampled (the client's tracked questions asked by
        Seolyticize, no volume); the two are never summed. For platforms other than
        google and chat_gpt only sampled rows exist and the call is free. A paid lookup
        on the client's account unless anyone read the same thing recently (spend says
        which); quote it with estimate_cost. (about $0.10 a call) Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_ai_prompt_research", _present({"clientId": client_id, "keyword": keyword, "platform": platform, "limit": limit, "includeSampled": include_sampled, "sampledDays": sampled_days, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_referrals(self, *, client_id: str, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Visits AI assistants send. Visits from AI assistants — ChatGPT (chatgpt.com,
        chat.openai.com), Perplexity, Gemini, Copilot, Claude, Google AI Mode (where the
        referrer shows it), Grok, Meta AI, DeepSeek and others — as an AI channel: from
        the cookieless analytics, visits by assistant, their share of all visits, the
        landing pages they arrive on and the conversions they bring (goal events); from
        GA4, sessions by source / medium, landing pages and key events and revenue for
        the same sources. Answers 'how much traffic does ChatGPT send us', 'which pages
        do assistants send people to' and 'do AI visitors convert'. Free."""
        return self.call("get_ai_referrals", _present({"clientId": client_id, "days": days, "limit": limit}))

    def get_ai_search_volume(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """How often a topic is asked of AI. Estimated monthly AI-assistant search volume
        for up to 1,000 keywords, with 12 months of history. Answers 'how much is this
        asked in AI search' and 'which topics matter in AI answers'. A paid lookup on
        the client's account unless anyone read the same thing recently (spend says
        which); quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_ai_search_volume", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_top_cited_domains(self, *, client_id: str, topic: str, platform: Optional[Literal["google", "chat_gpt", "claude", "gemini", "perplexity", "copilot", "grok", "meta_ai", "deepseek", "ai_mode"]] = None, limit: Optional[int] = None, include_sampled: Optional[bool] = None, sampled_days: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who AI answers cite on a topic. The domains AI answers cite most for questions
        about a topic, with how often and the AI search volume behind it, the client's
        own marked — the outreach, PR and content targets for AI visibility. Answers
        'which sites does AI trust on this topic'. Rows carry source: dataforseo (real
        users' prompts, with AI search volume) or sampled (the client's tracked
        questions asked by Seolyticize, no volume); the two are never summed. For
        platforms other than google and chat_gpt only sampled rows exist and the call is
        free. A paid lookup on the client's account unless anyone read the same thing
        recently (spend says which); quote it with estimate_cost. (about $0.10 a call)
        Can spend: pass max_cost_micros to cap it."""
        return self.call("get_ai_top_cited_domains", _present({"clientId": client_id, "topic": topic, "platform": platform, "limit": limit, "includeSampled": include_sampled, "sampledDays": sampled_days, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_ai_visibility(self, *, client_id: str) -> Any:
        """Get AI assistant visibility. How often the client's brand appears in AI
        assistant answers versus competitors, and what kind of pages those answers were
        built from. Answers 'are we visible in ChatGPT, Copilot, Gemini and Claude' and
        'what do we have to be on to get cited'."""
        return self.call("get_ai_visibility", _present({"clientId": client_id}))

    def get_ai_visibility_answer(self, *, client_id: str, prompt_id: str, model: Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"], captured_at: str) -> Any:
        """Read one AI answer in full. The full text one assistant gave to one question in
        one check, with the pages it cited, where each tracked brand appears in it, and
        how it described each (sentiment by brand, empty when not judged). found is
        false when that answer was never captured or has aged out (answers are kept 13
        months). Answers 'what exactly did ChatGPT say'. Free."""
        return self.call("get_ai_visibility_answer", _present({"clientId": client_id, "promptId": prompt_id, "model": model, "capturedAt": captured_at}))

    def get_ai_visibility_results(self, *, client_id: str, captured_at: Optional[str] = None, topic: Optional[str] = None, segment: Optional[Literal["branded", "neutral"]] = None) -> Any:
        """AI visibility results, answer by answer. One check (the latest unless capturedAt
        names one from get_ai_visibility_runs), as a row per question and assistant: the
        question's topic and whether it is branded, whether the client was named, where
        in the answer (character offset; earlier is more prominent), whether its site
        was cited, how the answer described it (clientSentiment positive / neutral /
        negative with a one-line note; null when not named or not judged), and which
        other brands were named, in order. summary gives mention rate, citations and
        sentiment overall, neutral against branded, and per topic. Filter by topic or
        segment. Answers 'which questions are we missing from' and 'how do assistants
        talk about us'. Free."""
        return self.call("get_ai_visibility_results", _present({"clientId": client_id, "capturedAt": captured_at, "topic": topic, "segment": segment}))

    def get_ai_visibility_runs(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """AI visibility checks so far. Lists the client's checks, newest first: when, how
        many answers, which assistants, and in how many the client's own brand was named
        (mentionRate; null when no brand is marked as the client's), and the same rate
        on neutral questions only (neutralMentionRate), the one branded questions cannot
        flatter. Answers 'when did we last check, and how did it go'. Free."""
        return self.call("get_ai_visibility_runs", _present({"clientId": client_id, "limit": limit}))

    def get_ai_visibility_sentiment(self, *, client_id: str, days: Optional[int] = None, topic: Optional[str] = None, segment: Optional[Literal["branded", "neutral"]] = None) -> Any:
        """How AI answers describe each brand. Sentiment over the last N days (default 30):
        for every tracked brand, how many answers that named it described it positively,
        neutrally or negatively, net score ((positive − negative) / judged) and how many
        were never judged; the client's split per assistant; and the latest negative and
        positive descriptions of the client, each with its question and assistant.
        Answers 'do assistants recommend us or warn people off'. Free; unjudged answers
        can be filled in with assess_ai_visibility_sentiment."""
        return self.call("get_ai_visibility_sentiment", _present({"clientId": client_id, "days": days, "topic": topic, "segment": segment}))

    def get_ai_visibility_setup(self, *, client_id: str) -> Any:
        """AI visibility setup. Reads what is tracked for a client: the questions (with
        their market, topic, and whether each is branded — names a tracked brand — or
        neutral, worked out automatically unless overridden), the topics and the
        branded/neutral split, the brands looked for (which one is the client's own),
        the schedule (cadence, which assistants, last run, whether sentiment is judged),
        and which assistants this agency can ask at all and how (its own key or its
        proxy pool). Answers 'what are we measuring in AI assistants'. Free."""
        return self.call("get_ai_visibility_setup", _present({"clientId": client_id}))

    def get_ai_visibility_trend(self, *, client_id: str, days: Optional[int] = None, topic: Optional[str] = None, segment: Optional[Literal["branded", "neutral"]] = None) -> Any:
        """Is AI visibility improving. The client's own mention rate over the last N days
        (default 28) against the N days before, overall and per assistant, counted by
        answer, with how many answers each side rests on. Filter by topic, or segment
        neutral for the rate on questions naming no brand. Answers 'are we being
        recommended more than last month'. Free."""
        return self.call("get_ai_visibility_trend", _present({"clientId": client_id, "days": days, "topic": topic, "segment": segment}))

    def get_anchor_distribution(self, *, client_id: str, domain: Optional[str] = None, source: Optional[Literal["auto", "vendor", "index"]] = None, limit: Optional[int] = None, money_terms: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Anchor text mix. The anchor texts a domain is linked with, each classed as
        branded, a bare URL, generic (click here, read more), empty (images) or other
        (usually keyword-rich), and the mix by referring domains, with bands: each share
        against its natural range — branded 30–50% (flagged under 15%), URL 15–25%,
        generic 10–20%, exact match 3–10% (flagged over 15%), partial match 5–15%
        (flagged over 25%); exact and partial are told apart from other only with
        moneyTerms, the commercial phrases targeted. Answers 'does our link profile look
        natural' and 'what do they rank with'. source index is free: our own link index
        (our crawls, client crawls' outlinks, Common Crawl, Bing). auto answers from the
        index when it holds 50+ links to the domain (or, for referring domains, a
        complete pass of Common Crawl's domain graph), and otherwise asks the vendor — a
        paid lookup on the client's account unless anyone bought it in the last week;
        coverage says which answered. vendor always asks the vendor. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_anchor_distribution", _present({"clientId": client_id, "domain": domain, "source": source, "limit": limit, "moneyTerms": money_terms, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_anchor_overlap(self, *, client_id: str, crawl_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """One anchor, several pages. Descriptive anchor texts used for links to more than
        one page — the site telling search engines that two pages are about the same
        words, which splits their ranking (cannibalization through links). Generic
        anchors (read more, click here) are left out. Answers 'are our internal links
        confusing Google'. Free."""
        return self.call("get_anchor_overlap", _present({"clientId": client_id, "crawlId": crawl_id, "limit": limit}))

    def get_app_keyword_gap(self, *, client_id: str, store: Literal["app_store", "google_play"], app_id: str, competitors: Optional[List[str]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Keywords competitor apps rank for and ours does not. The store search keywords
        competitor apps rank for and the app does not, with search volume and each
        competitor's rank, from DataForSEO Labs (keywords for app; US English is what
        the vendor covers). With no competitors given, the vendor's own list of the
        app's competitors (top five) is used. Difficulty is not published for app
        keywords, so the best competitor rank stands in. Answers 'which keywords do
        rival apps rank for that we don't'. One read per app. A paid lookup on the
        client's account (spend says how much); quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_app_keyword_gap", _present({"clientId": client_id, "store": store, "appId": app_id, "competitors": competitors, "locationCode": location_code, "languageCode": language_code, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_app_metrics(self, *, client_id: str, engine: Literal["app_store", "google_play"], app_ids: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """How visible apps are in an app store. For up to 1,000 apps in the App Store
        (numeric ids, from /id… in the store URL) or Google Play (package names): how
        many search results pages each appears on, how many at #1, #2–3, #4–10 and
        #11–100, and the total search volume of those keywords, from DataForSEO Labs (US
        English only). Answers 'how visible is our app against these competitors'.
        get_ranked_keywords with engine app_store or google_play lists one app's
        keywords. A paid lookup on the client's account unless anyone read the same
        thing recently (spend says which); quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_app_metrics", _present({"clientId": client_id, "engine": engine, "appIds": app_ids, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_audit_performance(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """Speed in the audit. How fast the audited site is, as recorded when the crawl
        finished. Lab: a Lighthouse run (mobile) of the homepage and one page of each of
        the largest URL templates, with performance, accessibility, SEO and
        best-practices scores (0–100), LCP, TBT and CLS — one synthetic load each, from
        a Google datacentre. Field: the origin's Core Web Vitals from the Chrome UX
        Report — LCP, INP and CLS at the 75th percentile of real visits over 28 days,
        per phone and desktop, graded and with Google's pass/fail. Each page also
        carries diagnostics (where the time went: the LCP element and its subparts —
        TTFB, resource load delay, resource load duration, element render delay — DOM
        size, long tasks, main-thread work by kind, script execution, render-blocking
        requests, unused JavaScript and CSS, third parties, and the INP breakdown when
        the run interacted, which a PageSpeed run never does), and lab.fixes merges the
        pages' findings into one list ranked by estimated saving, with the pages each
        affects. Missing figures say why (no key, too few visits). crawlId defaults to
        the latest complete crawl. Answers 'is the site fast', 'which template is slow',
        'what should we fix first for speed' and 'do we pass Core Web Vitals'. Free."""
        return self.call("get_audit_performance", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_audit_summary(self, *, client_id: str, crawl_id: Optional[str] = None, indexable_only: Optional[bool] = None) -> Any:
        """Get site audit summary. Technical issues one crawl found, grouped by rule: each
        with its name, severity, category, how many pages it affects and howToFix.
        Answers 'what is broken on the site'. crawlId defaults to the latest completed
        crawl. Then list_issue_pages shows which pages an issue is on. indexableOnly
        (default true) leaves out findings on pages search engines will not index as
        themselves — noindexed, not answering 200, or canonicalised elsewhere — except
        the findings that explain why; pass false to see everything. Findings accepted
        as intentional (accept_issue) are taken out of the counts and listed apart in
        accepted, each with its reason; with path owners set (set_path_owners), each
        issue says how its pages split between owners (owners) and byOwner totals them."""
        return self.call("get_audit_summary", _present({"clientId": client_id, "crawlId": crawl_id, "indexableOnly": indexable_only}))

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

    def get_backlink_health(self, *, client_id: str, money_terms: Optional[List[str]] = None, spam_scores: Optional[Dict[str, Any]] = None, fetch_spam_scores: Optional[bool] = None, industry: Optional[Literal["saas", "ecommerce", "local", "publisher", "agency"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """How healthy is the link profile. Scores the client's link profile 0–100 (a
        heuristic, said so) from seven factors, each good, warn or critical with its
        figures and the source they came from (the vendor's synced index, our own link
        index, the domain graph): referring domains (20: over 100 good, under 20
        critical), quality distribution (20: the linking sites' authority, and domain
        diversity — one site over 10% of the links warns, over 25% is critical), anchor
        naturalness (15: the anchor bands of get_anchor_distribution), toxic ratio (20:
        the share of linking sites get_toxic_link_risk calls toxic), velocity (10: a
        fall in referring domains of over 20% a quarter is critical), follow ratio (5:
        over 60% followed good, under 40% critical) and geographic relevance (10: the
        linking sites' TLD and country mix against the client's market; 80% or more from
        other countries flags a private network). Each factor carries its source's
        confidence (DataForSEO 1.0, our link index 0.7, Common Crawl 0.5), which scales
        its weight; a number only when at least four factors have data, and never from
        presence-only sources alone (NOT ASSESSED); otherwise INSUFFICIENT DATA (X/7).
        industry (saas, ecommerce, local, publisher, agency) judges the anchors against
        that industry's natural ranges. Also the profile's toxic signals: 50+ directory
        links, linking pages with 10,000+ outbound links, more than 50 links from one
        site, linking pages under 100 words, reciprocal links. Pass moneyTerms to tell
        exact and partial-match anchors apart. Spam scores sharpen the toxic ratio:
        fetchSpamScores: true buys them inside this call (one paid DataForSEO request of
        up to 1,000 linking sites, the price of get_backlink_spam_scores; sites scored
        in the last 30 days are reused free; quote it with estimate_cost or dryRun
        first), or pass spamScores you already have. Answers 'how healthy are our
        backlinks' and 'is our link profile at risk'. Free without fetchSpamScores. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("get_backlink_health", _present({"clientId": client_id, "moneyTerms": money_terms, "spamScores": spam_scores, "fetchSpamScores": fetch_spam_scores, "industry": industry, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_backlink_history(self, *, client_id: str, target: Optional[str] = None, from_: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A domain's backlinks over time. Month by month for any domain: backlinks,
        referring domains, new and lost backlinks and referring domains, and rank, from
        DataForSEO's index (back to 2019; new and lost from May 2021). Answers 'is their
        link profile growing', 'when did we lose those links'. A paid lookup on the
        client's account unless anyone read the same thing recently (spend says which);
        quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_backlink_history", _present({"clientId": client_id, "target": target, "from": from_, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_backlink_spam_scores(self, *, client_id: str, domains: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """The vendor's spam scores for linking sites. The data vendor's own spam score
        (0–100, null when it has none) for each domain you pass — usually the sources
        from get_backlink_audit. A second opinion beside ours: a link both call bad is
        one to act on. Paid, one purchase per call however many domains (up to 1000):
        quote it with estimate_cost and get the user's go-ahead first. Answers 'what
        does the vendor think of these links'. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("get_backlink_spam_scores", _present({"clientId": client_id, "domains": domains, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_backlinks(self, *, client_id: str, domain: Optional[str] = None, source: Optional[Literal["auto", "vendor", "index"]] = None, limit: Optional[int] = None, mode: Optional[Literal["all", "new", "lost"]] = None, days: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Backlinks, new and lost. The links to a domain, page to page, with anchor and
        follow status; mode new lists links first seen in the last days, lost those no
        longer seen since. Answers 'which links did we gain or lose this month' and
        'what links does this competitor have'. source index is free: our own link index
        (our crawls, client crawls' outlinks, Common Crawl, Bing). auto answers from the
        index when it holds 50+ links to the domain (or, for referring domains, a
        complete pass of Common Crawl's domain graph), and otherwise asks the vendor — a
        paid lookup on the client's account unless anyone bought it in the last week;
        coverage says which answered. vendor always asks the vendor. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_backlinks", _present({"clientId": client_id, "domain": domain, "source": source, "limit": limit, "mode": mode, "days": days, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_batch_analysis(self, *, client_id: str, targets: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Compare many domains at once. For up to 200 domains (or pages) at once:
        DataForSEO rank, backlinks, referring domains, organic traffic and organic
        keywords, in one table. For stored figures without a purchase,
        batch_domain_metrics. Answers 'size these sites up side by side' and 'which of
        these prospects are worth it'. Four bulk reads, whatever the number of targets.
        A paid lookup on the client's account unless anyone read the same thing this
        week (spend says which); quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_batch_analysis", _present({"clientId": client_id, "targets": targets, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_best_pages_by_links(self, *, client_id: str, domain: Optional[str] = None, source: Optional[Literal["auto", "vendor", "index"]] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Pages that attract links. A domain's pages by how many domains link to them. Run
        it on competitors to see what kind of content earns links in a niche — the
        content worth making. Answers 'what do people link to'. source index is free:
        our own link index (our crawls, client crawls' outlinks, Common Crawl, Bing).
        auto answers from the index when it holds 50+ links to the domain (or, for
        referring domains, a complete pass of Common Crawl's domain graph), and
        otherwise asks the vendor — a paid lookup on the client's account unless anyone
        bought it in the last week; coverage says which answered. vendor always asks the
        vendor. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_best_pages_by_links", _present({"clientId": client_id, "domain": domain, "source": source, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

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

    def get_bing_crawl_health(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """How Bing crawls the site. Bing's crawl stats by day (pages crawled, in index,
        errors by HTTP class, blocked by robots.txt, DNS failures and timeouts), the
        URLs Bing reports crawl issues for with the issues counted by type, and the
        pages or directories blocked from Bing's results. Answers 'is Bing having
        trouble crawling us' and 'did someone hide a page from Bing'. Bing's API has no
        penalty or manual-action feed, so none is reported. Free."""
        return self.call("get_bing_crawl_health", _present({"clientId": client_id, "limit": limit}))

    def get_bing_inbound_links(self, *, client_id: str, url: Optional[str] = None, page: Optional[int] = None) -> Any:
        """Links Bing knows point at the site. Bing's own link data from Webmaster Tools:
        without url, the client's pages that have inbound links and how many each has;
        with url (a page on the client's site), the pages linking to it and their anchor
        text. Paged as Bing pages it (page from 0; totalPages says how many). Answers
        'which of our pages earn links, according to Bing' and 'who links to this page'.
        Free."""
        return self.call("get_bing_inbound_links", _present({"clientId": client_id, "url": url, "page": page}))

    def get_bing_keyword_research(self, *, client_id: str, keyword: str, country: Optional[str] = None, language: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None) -> Any:
        """Bing's own search volume for a term. Bing Webmaster Tools' keyword research on
        the agency's key: the term's Bing impressions week by week (exact and broad
        match) and related terms with their impressions over a date range. Bing
        publishes real counts rather than bands. Answers 'how often is this searched on
        Bing' and 'what else do Bing users search around it'. country is a two-letter
        code, language a tag such as en-GB. Free."""
        return self.call("get_bing_keyword_research", _present({"clientId": client_id, "keyword": keyword, "country": country, "language": language, "from": from_, "to": to}))

    def get_bing_performance(self, *, client_id: str) -> Any:
        """What Bing Webmaster Tools reports. The client's site as Bing reports it, on the
        agency's Webmaster Tools key: daily clicks and impressions, page and query
        stats, crawl stats (pages crawled, in index, errors by status), crawl issues per
        URL, sitemaps and feeds, and the URL submission quota. Answers 'how is this site
        doing in Bing'. These are Bing's numbers about Bing's searchers and must never
        be added to Google's. Each part is separately present or failed; connected is
        false when the agency has no Bing key."""
        return self.call("get_bing_performance", _present({"clientId": client_id}))

    def get_bing_search_stats(self, *, client_id: str, dimension: Optional[Literal["query", "page"]] = None, query: Optional[str] = None, page: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Bing queries or pages, week by week. Bing Webmaster Tools' query stats or page
        stats for the client's site, each row with its clicks, impressions and position
        and its weekly history (Bing publishes weekly, about six months back). Give
        query to see which pages answered that one query, or page to see which queries
        that one page answered. Answers 'what do people find us for on Bing' and 'which
        page does Bing show for this'. Bing's numbers about Bing's searchers, on the
        agency's Webmaster Tools key; never add them to Google's. Free."""
        return self.call("get_bing_search_stats", _present({"clientId": client_id, "dimension": dimension, "query": query, "page": page, "limit": limit}))

    def get_brand_mentions(self, *, client_id: str, keyword: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Find recent mentions of a brand or phrase. Who has written about a brand or
        phrase lately — the page, its title and snippet, when it was published, and how
        it read (positive, negative or neutral) — one result per publishing domain, up
        to 50. Answers 'who is talking about us' and finds unlinked mentions worth
        asking for a link. A paid lookup on the client's account: quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_brand_mentions", _present({"clientId": client_id, "keyword": keyword, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_brand_split(self, *, client_id: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, from_: Optional[str] = None, to: Optional[str] = None, interval: Optional[Literal["day", "week", "month"]] = None, country: Optional[str] = None) -> Any:
        """Branded vs non-branded search. Google search clicks and impressions split into
        branded (the query names the client) and non-branded, by day, week or month,
        with the property total and the anonymised remainder Google withholds queries
        for. Answers 'is non-branded traffic growing' — the number content and SEO work
        actually move. Brand terms come from the client brief (update_client_brief
        brandTerms), or the client's name and domain. searchType picks web (default),
        image, video or news; Discover and Google News have no queries to split. Free."""
        return self.call("get_brand_split", _present({"clientId": client_id, "searchType": search_type, "from": from_, "to": to, "interval": interval, "country": country}))

    def get_branding(self) -> Any:
        """Read the agency's branding. The agency's name, logo address and primary colour:
        what clients see on reports and portal links. Answers 'what will this report
        look like to the client'. Empty strings where nothing is set."""
        return self.call("get_branding", {})

    def get_broken_backlinks(self, *, client_id: str, source: Optional[Literal["auto", "vendor", "index"]] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Links to broken pages. Links from other sites to the client's pages that no
        longer work (4xx, or not answering), grouped by page, with the closest live page
        to redirect each to — links already earned, reclaimed with one redirect. Answers
        'which links are we wasting'. Status comes from the latest crawl, and pages it
        did not crawl are checked. source index is free: our own link index (our crawls,
        client crawls' outlinks, Common Crawl, Bing). auto answers from the index when
        it holds 50+ links to the domain (or, for referring domains, a complete pass of
        Common Crawl's domain graph), and otherwise asks the vendor — a paid lookup on
        the client's account unless anyone bought it in the last week; coverage says
        which answered. vendor always asks the vendor. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_broken_backlinks", _present({"clientId": client_id, "source": source, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_budget_status(self, *, client_id: str) -> Any:
        """A client's budget and month-end forecast. A client's monthly budget (null when
        none is set), what it has spent this month, what is left, when the month resets
        and the alert share, plus projection: an estimate of month-end spend from the
        paid work already scheduled — each rank tracker's cadence × keywords × devices ×
        price, AI visibility checks on their cadence, and alert rules with their paid
        source on — priced from the same ceilings estimate_cost quotes, so the real
        figure is usually lower. Answers 'how much budget is left' and 'will this client
        go over this month' before any paid call. set_budget changes the budget;
        get_client_costs says what the spend went on. Free."""
        return self.call("get_budget_status", _present({"clientId": client_id}))

    def get_business_posts(self, *, client_id: str, business: Optional[str] = None, task_id: Optional[str] = None, depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Any business's Google posts. The posts (updates, offers, events) any business
        has published on its Google Business Profile, newest first: text, date, image,
        links and the post's address, with how many there are, when the latest went up
        and how many in the last 90 days. Collecting takes a few minutes: the first call
        (with business) queues it and returns a taskId — that call is the paid one — and
        calling again with the taskId collects it for free (status pending until ready).
        Answers 'how often does this competitor post on Google' and 'what are they
        promoting'. A paid lookup on the client's account unless anyone read the same
        thing recently; quote it with estimate_cost. Can spend: pass max_cost_micros to
        cap it."""
        return self.call("get_business_posts", _present({"clientId": client_id, "business": business, "taskId": task_id, "depth": depth, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_business_profile(self, *, client_id: str, business: str, location_code: Optional[int] = None, language_code: Optional[str] = None, lat: Optional[float] = None, lng: Optional[float] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Any business's Google profile. The Google Business Profile of any business,
        found by name or by cid / place_id: categories, address, phone, site,
        coordinates, rating and its spread, review count, hours, attributes, photos,
        whether it is claimed, the topics reviewers mention and the businesses people
        also search. Gives the place_id and coordinates add_local_location needs.
        Answers 'what does this competitor's listing have that ours lacks'. A paid
        lookup on the client's account unless anyone read the same thing recently; quote
        it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_business_profile", _present({"clientId": client_id, "business": business, "locationCode": location_code, "languageCode": language_code, "lat": lat, "lng": lng, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_business_questions(self, *, client_id: str, business: str, limit: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, lat: Optional[float] = None, lng: Optional[float] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A business's Google Q&A. The questions people asked on any business's Google
        listing, with the answers and who gave them, and how many are unanswered.
        Answers 'what do customers ask about us' and 'which questions should we answer
        on our profile'. A paid lookup on the client's account unless anyone read the
        same thing recently; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_business_questions", _present({"clientId": client_id, "business": business, "limit": limit, "locationCode": location_code, "languageCode": language_code, "lat": lat, "lng": lng, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_business_reviews(self, *, client_id: str, business: Optional[str] = None, task_id: Optional[str] = None, depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Any business's Google reviews. Google reviews of any business (up to 500, newest
        first) with the rating, text, date, author and whether the owner replied.
        Collecting takes a minute or two: the first call (with business) queues it and
        returns a taskId — that call is the paid one — and calling again with the taskId
        collects it for free (status pending until ready). For the client's own
        locations, sync_local_reviews keeps them stored. Answers 'what do customers
        complain about at this competitor'. A paid lookup on the client's account unless
        anyone read the same thing recently; quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_business_reviews", _present({"clientId": client_id, "business": business, "taskId": task_id, "depth": depth, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_cannibalization(self, *, client_id: str) -> Any:
        """Get cannibalization. Keywords where several of the client's own pages compete in
        the same result, each with the page the keyword registry says owns it (owner,
        null when unregistered) and the page that should win (shouldOwn: the registered
        owner, else the best-placed page). Answers 'where are we competing with
        ourselves' and 'which page should own this query'. set_keyword_owners registers
        owners."""
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
        account'. The budget, what is left of it and a month-end forecast are
        get_budget_status. Amounts are US dollars."""
        return self.call("get_client_costs", _present({"clientId": client_id, "sinceDays": since_days}))

    def get_client_integrations(self, *, client_id: str) -> Any:
        """Which consoles are connected for a client. Whether a client's Google Search
        Console and Google Analytics properties are connected and syncing, with the last
        sync error, and whether IndexNow is set up. backfill gives Search Console's
        sixteen-month history: the range asked for (from, to), how far it has got
        (collectedThrough, progress), its status — pending, running, retrying or
        complete — the rows stored and the days they span (rowsStored, storedFrom,
        storedThrough), and a note saying where Google's data for the property begins
        when it holds less than sixteen months. Answers 'is Search Console connected for
        this client' and 'is the history in yet'. Never returns tokens."""
        return self.call("get_client_integrations", _present({"clientId": client_id}))

    def get_competitor_broken_pages(self, *, client_id: str, domain: str, source: Optional[Literal["auto", "vendor", "index"]] = None, dofollow_only: Optional[bool] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A competitor's dead pages that still have links. A domain's pages that answer
        404 or 410 but that other sites still link to, with how many referring domains
        (and how many of them dofollow) each still has — the broken-link-building
        targets: offer the linking sites your page instead. Run on the client's own
        domain it lists links to reclaim with a redirect (get_broken_backlinks adds the
        redirect target). source vendor reads DataForSEO's index; index reads our own
        crawl, free but only pages we have fetched; auto asks the vendor and falls back
        to the index. Answers 'which of their dead pages could we take the links of'.
        source vendor (and auto, when a provider is connected) is a paid lookup on the
        client's account unless anyone read it this week; quote it with estimate_cost.
        index is free. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_competitor_broken_pages", _present({"clientId": client_id, "domain": domain, "source": source, "dofollowOnly": dofollow_only, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_competitor_new_pages(self, *, client_id: str, days: Optional[int] = None, competitors: Optional[List[str]] = None, limit: Optional[int] = None) -> Any:
        """What competitors published. New and updated pages on competitors' sites, from
        their sitemaps (read daily for every competitor a tracker watches, and read now
        for any not yet watched), grouped by section — 'competitor X published 14 pages
        under /guides this week'. Answers 'what are they writing about' and 'what did
        they just launch'. competitors overrides the tracked ones. Free."""
        return self.call("get_competitor_new_pages", _present({"clientId": client_id, "days": days, "competitors": competitors, "limit": limit}))

    def get_competitor_page_changes(self, *, client_id: str, tracker_id: Optional[str] = None, days: Optional[int] = None) -> Any:
        """Changes to pages that outrank us. Pages that rank above the client for its
        tracked keywords whose title, H1, length or sections changed — read from
        snapshots taken every few days. Answers 'what did the page that beat us change'.
        Free."""
        return self.call("get_competitor_page_changes", _present({"clientId": client_id, "trackerId": tracker_id, "days": days}))

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

    def get_content_audit(self, *, client_id: str, verdict: Optional[Literal["keep", "update", "merge", "review", "no_search_data"]] = None, limit: Optional[int] = None) -> Any:
        """Content audit: keep, update, merge or review each page. A verdict for every page
        meant to rank in the latest crawl, from its Google search over the last 90 days
        against the 90 before (page-level Search Console, top query included), its
        length and whether it nearly duplicates another page: keep (earning and steady),
        update (losing clicks, seen but rarely clicked, or thin for the demand it has),
        merge (near-duplicate of another page) review (no search demand in six months —
        improve it, fold it into another, or noindex it, after checking its links and
        conversions; never deleted on this alone) or no_search_data (no Search Console
        rows for it, and too little history to call that absent demand). Each with the
        reason; excluded counts the crawled pages left out (non-200, noindex, canonical
        elsewhere, parameter copies). Without Search Console only merge is judged.
        Answers 'which pages should we refresh, merge or prune'. Free."""
        return self.call("get_content_audit", _present({"clientId": client_id, "verdict": verdict, "limit": limit}))

    def get_content_decay(self, *, client_id: str) -> Any:
        """Get decaying content. Pages losing the traffic they used to earn, over
        consecutive periods. Answers 'what should we refresh'."""
        return self.call("get_content_decay", _present({"clientId": client_id}))

    def get_content_gap(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get content gap. Competitor pages that own a cluster of keywords the client does
        not cover. Answers 'what page should we build next' — use this rather than
        keyword gap when planning content."""
        return self.call("get_content_gap", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_content_groups(self, *, client_id: str, days: Optional[int] = None, compare: Optional[Literal["previous", "year"]] = None, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, groups: Optional[List[Dict[str, Any]]] = None, country: Optional[str] = None, device: Optional[Literal["DESKTOP", "MOBILE", "TABLET"]] = None) -> Any:
        """Search traffic by section. Google search clicks, impressions and position rolled
        up by section of the site, two periods compared. Answers 'how is the blog doing
        against the guides' and 'which template is losing traffic'. groups are matched
        in order against each page's path, first match wins (* matches anything, so
        '/blog/*'); without groups, pages are grouped by their first path segment.
        searchType reads image, video, news, Discover or Google News instead of web.
        Free."""
        return self.call("get_content_groups", _present({"clientId": client_id, "days": days, "compare": compare, "searchType": search_type, "groups": groups, "country": country, "device": device}))

    def get_conversions(self, *, client_id: str, source: Optional[Literal["web_analytics", "ga4"]] = None, by: Optional[Literal["landing_page", "source", "referrer"]] = None, channel: Optional[Literal["all", "search", "ai"]] = None, goals: Optional[List[str]] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Conversions by landing page and source. Conversions (sign-ups, purchases, any
        goal) by the page a visit landed on, its source or its referrer, with visits,
        converting visits, conversion rate and value — and, by landing page, the Search
        Console queries that bring those visits. Answers 'which pages and queries
        actually make money' and 'what is organic search worth'. source web_analytics
        uses the cookieless analytics' custom events (goals: the event names; default
        every event; value from a 'value' property); ga4 uses GA4's key events on
        organic sessions. channel narrows to search engines or AI assistants. Free."""
        return self.call("get_conversions", _present({"clientId": client_id, "source": source, "by": by, "channel": channel, "goals": goals, "days": days, "limit": limit}))

    def get_costs(self, *, since_days: Optional[int] = None) -> Any:
        """Vendor spend by client. What the agency spent on data vendors per client over
        recent days, with request counts. Answers 'which clients cost us the most'.
        Amounts are US dollars."""
        return self.call("get_costs", _present({"sinceDays": since_days}))

    def get_crawl_budget(self, *, client_id: str, days: Optional[int] = None, bot: Optional[str] = None) -> Any:
        """Where crawlers spend their visits. From the client's connected logs over the
        last days (default 30): crawler requests by URL template (the site section, not
        the page), each with its share of all crawler requests, how much went on errors
        and redirects, and which crawlers; plus per crawler how many requests were
        verified (reverse DNS or published IP ranges), spoofed (claimed the name, failed
        the check — left out of every figure) or not checkable. Assets are left out. bot
        narrows to one crawler (googlebot, bingbot, gptbot…). Answers 'what is Googlebot
        wasting its time on' and 'how much of our crawl budget goes on parameter URLs'.
        Free."""
        return self.call("get_crawl_budget", _present({"clientId": client_id, "days": days, "bot": bot}))

    def get_crawl_settings(self, *, client_id: str) -> Any:
        """How the site is crawled. The client's crawl settings: mode (spider, list or
        sitemap), include and exclude URL patterns, page and depth limits, the user
        agent sent and the robots.txt group obeyed, speed (requests per second and
        concurrency), query parameters stripped from discovered URLs, custom extraction
        rules, JavaScript rendering (off, shells — only pages that look unrendered — or
        all, up to renderMaxPages a crawl), whether staging credentials are set (names
        only, never values), whether requests are signed with Web Bot Auth, and the
        crawl schedule (cadence, day, UTC hour and nextRunAt; weekly on Monday 02:00 UTC
        unless set_crawl_schedule changed it). Answers 'what does the crawl do
        differently for this site'. Free."""
        return self.call("get_crawl_settings", _present({"clientId": client_id}))

    def get_crawl_status(self, *, client_id: str, crawl_id: str) -> Any:
        """Get crawl status. Whether one crawl is running, complete or failed, with page
        and issue counts and the failure reason. Answers 'has the audit finished'."""
        return self.call("get_crawl_status", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_ctr_outliers(self, *, client_id: str, days: Optional[int] = None, min_impressions: Optional[int] = None, sigma: Optional[float] = None, limit: Optional[int] = None) -> Any:
        """Queries clicking far from what they should. Fits the site's own click-through
        rate by position bucket and device — and by results-page shape (AI Overview,
        featured snippet, map pack, shopping, video, plain) where rank captures say what
        the page showed — then lists Search Console queries more than sigma (default 2)
        standard deviations under it (a title or snippet problem: under, with the clicks
        missed) and over it (a snippet worth copying: over). Falls back to the published
        industry curve where the site has too few queries in a bucket, and model says
        which was used (site, published or mixed). Answers 'which snippets should we
        rewrite' and 'which titles work best'. Free."""
        return self.call("get_ctr_outliers", _present({"clientId": client_id, "days": days, "minImpressions": min_impressions, "sigma": sigma, "limit": limit}))

    def get_demand_matrix(self, *, client_id: str, pattern: str, slots: Dict[str, Any], location_code: Optional[int] = None, language_code: Optional[str] = None, min_volume: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Demand for every combination. Search volume, difficulty and CPC for every
        combination of a pattern's slots — 'receive sms {service} {country}' with
        services and countries — up to 500, with the client's ranking page and position
        for each from Search Console and a verdict: write (demand, no page), improve (a
        page beyond the top ten), have (top ten) or skip (no demand). Answers 'which of
        these template pages deserve to exist'. Volumes any agency bought before are
        reused free; the rest is a paid keyword lookup on the client's account, in
        batches. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_demand_matrix", _present({"clientId": client_id, "pattern": pattern, "slots": slots, "locationCode": location_code, "languageCode": language_code, "minVolume": min_volume, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_deploy_hook(self, *, client_id: str) -> Any:
        """Get the deploy hook's status. Answers 'did the last deploy notify search
        engines'. Whether the client has a deploy hook, how many sitemap pages it knows,
        and what its last call did. Never the URL itself. Free."""
        return self.call("get_deploy_hook", _present({"clientId": client_id}))

    def get_disavow_history(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """The client's saved disavow files. The disavow files saved for the client, newest
        first, with how many domains and URLs each names, and what the newest changed
        against the one before. Answers 'what did we disavow last time' and 'what
        changed in the disavow file'. get_toxic_link_risk lists risky sites that
        appeared since. Free."""
        return self.call("get_disavow_history", _present({"clientId": client_id, "limit": limit}))

    def get_domain_facts(self, *, domain: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What the open web says about a domain. Registration date and registrar from the
        registry, position on the Tranco top-sites list, when the Internet Archive first
        captured it, and the subdomains its certificates have announced, plus
        topicShift: the homepage's title and description as first archived against
        today's, crossed with the registration date, as a risk level (high: a different
        topic on a domain registered again after the archive first saw it, registered
        recently, or registered five or more years ago — the expired-domain abuse
        pattern; medium: a changed topic on a registration two to five years old;
        unknown when either page could not be read; a heuristic). Answers 'how old and
        how big is this, and what else is on it' and 'was this domain bought and
        repurposed' for any domain, free and without touching a vendor. Each figure is
        absent far more often than present, and an absence is never a zero: no registry
        record, not in the top million, never archived. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_domain_facts", _present({"domain": domain, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_domain_keyword_gap(self, *, client_id: str, competitors: List[str], target: Optional[str] = None, mode: Optional[Literal["missing", "shared", "weak"]] = None, min_volume: Optional[int] = None, limit: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Keyword gap against competitors. The keywords up to five competitors rank for in
        Google and the client does not (mode missing), that both rank for (shared), or
        where the client ranks below them (weak) — merged across the competitors, with
        volume, difficulty, CPC, intent, the client's position and each competitor's.
        Works for any domains, tracked or not, from DataForSEO's index; get_keyword_gap
        is the free reading from what the client's trackers already captured. Answers
        'what do our competitors rank for that we don't' and 'where are we losing to
        them'. One read per competitor. A paid lookup on the client's account unless
        anyone read the same thing this week (spend says which); quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_domain_keyword_gap", _present({"clientId": client_id, "target": target, "competitors": competitors, "mode": mode, "minVolume": min_volume, "limit": limit, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_domain_overview(self, *, client_id: str, target: Optional[str] = None, location_codes: Optional[List[int]] = None, language_code: Optional[str] = None, history_months: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A domain's organic and paid standing. For any domain: organic and paid keywords,
        estimated traffic and its value, the split of positions (top 3, 4–10, 11–100)
        and keywords new, up, down and lost — in one or more countries (locationCodes,
        up to 5) — and a monthly history (historyMonths, up to 36). Answers 'how big is
        this competitor', 'where do they get traffic' and 'is their traffic growing'. A
        paid lookup on the client's account unless anyone read the same thing recently
        (spend says which); quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_domain_overview", _present({"clientId": client_id, "target": target, "locationCodes": location_codes, "languageCode": language_code, "historyMonths": history_months, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_domain_technologies(self, *, domain: str) -> Any:
        """See what a domain is built with. The technologies our own crawler detected on
        any domain — CMS, analytics, commerce, CDN and so on — with the version most
        pages showed and how many pages showed it, as of the day it was last crawled.
        Answers 'what is this site built on'. Free. Null when our crawler has never
        fetched the domain, which says nothing about what it runs."""
        return self.call("get_domain_technologies", _present({"domain": domain}))

    def get_engine_capabilities(self, *, engines: Optional[List[Literal["google", "bing", "youtube", "amazon", "yandex", "baidu", "naver", "duckduckgo", "yahoo", "seznam", "app_store", "google_play"]]] = None, capabilities: Optional[List[Literal["rank_tracking", "live_serp", "search_volume", "keyword_difficulty", "keyword_ideas", "ranked_keywords", "top_pages", "content_profile", "serp_features", "serp_history", "webmaster_data", "url_submission"]]] = None) -> Any:
        """What can be done on each search engine. The matrix of what this product does on
        each engine — Google, Bing, YouTube, Amazon, Yandex, Baidu, Naver, DuckDuckGo,
        Yahoo, Seznam, App Store, Google Play — for rank tracking, live results, search
        volume, difficulty, keyword ideas, ranked keywords, top pages, content profiles,
        SERP features and history, webmaster data and URL submission. Each cell is
        supported (with the tools that do it), not_offered_by_engine (the engine
        publishes nothing to read) or not_built, with a note. Also lists the AI answer
        engines and whether their data is sampled by Seolyticize or from DataForSEO.
        Answers 'can you do X on Bing' and 'why is there no Naver index data'. Free."""
        return self.call("get_engine_capabilities", _present({"engines": engines, "capabilities": capabilities}))

    def get_engine_keyword_ideas(self, *, client_id: str, engine: Literal["bing", "amazon"], seeds: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Keyword ideas for Bing or Amazon. Keyword ideas around seed terms on another
        engine: engine bing reads DataForSEO's Bing keywords-for-keywords (with Bing
        volume, CPC, competition and monthly history; English, French and German),
        engine amazon reads DataForSEO Labs' Amazon related keywords (with Amazon search
        volume; one seed). Answers 'what do people search on Amazon around this product'
        and 'what are the Bing variations of this term'. Google ideas are
        keyword_explorer. A paid lookup on the client's account unless anyone read the
        same thing recently (spend says which); quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_engine_keyword_ideas", _present({"clientId": client_id, "engine": engine, "seeds": seeds, "locationCode": location_code, "languageCode": language_code, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_entity_coverage(self, *, client_id: str, keyword: str, url: Optional[str] = None, html: Optional[str] = None, markdown: Optional[str] = None, resolve: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """The entities a page should cover. The named entities (people, products, places,
        organisations, concepts) at least two of the ranking pages for a keyword cover,
        from their capitalised phrases, each resolved on Wikidata (resolve: true, free),
        whether the client's page (url, html or markdown; or none, to plan one) names
        it, a 0–100 coverage score, and the JSON-LD to add: about (the main entity) and
        mentions, with sameAs links to Wikidata and Wikipedia. Answers 'which entities
        does our page miss' and 'what sameAs and about schema should it carry'. Same
        cost as get_serp_content_profile. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_entity_coverage", _present({"clientId": client_id, "keyword": keyword, "url": url, "html": html, "markdown": markdown, "resolve": resolve, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_entity_pageviews(self, *, entity: str, from_: str, to: str, language: Optional[str] = None, granularity: Optional[Literal["daily", "monthly"]] = None) -> Any:
        """How many people looked a brand or topic up. Wikipedia article views for a brand
        or topic over a period, daily or monthly. Answers 'is interest in this name
        growing' with a complete count published by Wikimedia rather than a vendor's
        model or a panel sample. Returns nothing at all when Wikipedia has no article,
        which is the case for most small brands — and says which article it counted,
        because the closest article is not always the brand's own."""
        return self.call("get_entity_pageviews", _present({"entity": entity, "language": language, "granularity": granularity, "from": from_, "to": to}))

    def get_error_catalogue(self, *, code: Optional[str] = None) -> Any:
        """What every error code means. Every refusal code the API returns, with what it
        means and what to do about it — the same list as GET /api/v1/errors. Answers
        'what does spend_cap_exceeded mean'. Free."""
        return self.call("get_error_catalogue", _present({"code": code}))

    def get_extraction_results(self, *, client_id: str, crawl_id: Optional[str] = None, name: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
        """Custom extraction results. The values custom extraction (set_crawl_settings
        extractions) read off each page in a crawl, page by page; name narrows to one
        rule. Answers 'which pages have no author', 'what price does each product page
        show' and 'which posts are older than X'. Free."""
        return self.call("get_extraction_results", _present({"clientId": client_id, "crawlId": crawl_id, "name": name, "limit": limit, "offset": offset}))

    def get_forum_opportunities(self, *, client_id: str, keywords: Optional[List[str]] = None, days: Optional[int] = None, max_position: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Reddit, Quora and forum threads ranking for our keywords. Threads on Reddit,
        Quora and forums that rank in Google for the client's keywords, with the thread
        title, address and position, and whether Google shows it in its Discussions and
        forums box — where a helpful answer earns visibility and referral traffic the
        client's own page cannot. Answers 'which Reddit threads rank for our keywords'
        and 'where should we join the conversation'. With no keywords given, reads the
        tracked keywords' latest captured results pages, free. With keywords (up to 20),
        reads Google's results for each now: A paid lookup on the client's account
        unless anyone read the same thing recently (spend says which); quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_forum_opportunities", _present({"clientId": client_id, "keywords": keywords, "days": days, "maxPosition": max_position, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_freshness_queue(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """Pages to refresh first. The client's pages ranked by Search Console clicks at
        risk (a month's clicks, weighted by how many stale signals the page shows and
        doubled when it is already losing them) from going stale: the results page for
        its top query moved to newer content (the ranking pages' stored dates, at the
        median, over six months newer than the page's own), a past year in the title,
        past years in the text (with the sentence), a price or limit contradicting the
        client's registered facts, or no date on a page whose rivals are recent. Each
        with its reasons and priority. Answers 'what should we update this month'. Free:
        stored results pages and the latest crawl only."""
        return self.call("get_freshness_queue", _present({"clientId": client_id, "limit": limit}))

    def get_funnel_report(self, *, client_id: str, funnel_id: str, by: Optional[Literal["none", "channel", "landing_page", "source", "campaign", "ai_referrer", "query_cluster"]] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Funnel steps and drop-off. How many visits reached each step of a funnel in
        order, with the share of the first step and of the step before, overall and per
        channel, landing page, source, campaign, AI referrer or query cluster. Answers
        'where do people drop out between pricing and sign-up' and 'does search traffic
        finish the funnel'. Free."""
        return self.call("get_funnel_report", _present({"clientId": client_id, "funnelId": funnel_id, "by": by, "days": days, "limit": limit}))

    def get_ga4_audience(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, by: Optional[Literal["device", "country", "newVsReturning"]] = None, channel: Optional[Literal["organic", "all", "ai"]] = None) -> Any:
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

    def get_ga4_landing_pages(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all", "ai"]] = None) -> Any:
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
        dimensions and metrics, the last day with sessions, and Consent Mode v2 on each
        stream's site (an inline gtag consent default naming ad_user_data and
        ad_personalization; a consent platform or Tag Manager that may set it out of
        sight is named, not marked missing). findings lists problems, warnings and notes
        in plain words; a part that could not be read is reported as unread, not as
        fine. Answers 'can we trust this client's Analytics'. Refuses with a sentence
        when the client has not connected a GA4 property. Free."""
        return self.call("get_ga4_measurement_health", _present({"clientId": client_id}))

    def get_ga4_overview(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all", "ai"]] = None) -> Any:
        """Is organic traffic growing (GA4). Top-line sessions, users, engaged sessions,
        engagement rate, key events, transactions and revenue for organic search
        (channel "all" for every channel), against the previous period, plus a daily
        sessions and key-events line. Answers 'is organic traffic improving'. total
        holds the figures. Rows carry key, current (metrics by name) and previous (null
        when compare is false, metrics null where that period had no row). Also period,
        previousPeriod, currency, thresholded and folded. Refuses with a sentence when
        the client has not connected a GA4 property. Free."""
        return self.call("get_ga4_overview", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "channel": channel}))

    def get_ga4_page_performance(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, channel: Optional[Literal["organic", "all", "ai"]] = None) -> Any:
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

    def get_ga4_traffic_acquisition(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None, group_by: Optional[Literal["channel", "sourceMedium", "campaign", "aiSource"]] = None) -> Any:
        """Where traffic comes from (GA4). Sessions, users, engaged sessions, key events,
        transactions and revenue by channel group, source/medium or campaign (groupBy),
        against the previous period. Answers 'which channels grew or fell'. Rows carry
        key, current (metrics by name) and previous (null when compare is false, metrics
        null where that period had no row). Also period, previousPeriod, currency,
        thresholded and folded. Refuses with a sentence when the client has not
        connected a GA4 property. Free."""
        return self.call("get_ga4_traffic_acquisition", _present({"clientId": client_id, "from": from_, "to": to, "compare": compare, "limit": limit, "groupBy": group_by}))

    def get_geo_readiness(self, *, client_id: str, urls: Optional[List[str]] = None, top_pages: Optional[int] = None, brand_mentions: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """How ready the pages are to be cited in AI answers. A 0–100 generative-engine
        readiness score per page, for the pages given or the top pages by Search Console
        clicks (up to 20): citability 25 (an answer in the first 40–60 words of each H2
        section, self-contained 130–170-word passages, 'X is…' definitions, figures with
        a cited source, the most citable block in the first 30% of the page), structure
        20 (heading hierarchy, question headings, 2–4-sentence paragraphs, tables and
        lists), multimodal 15 (images, video, VideoObject markup, infographics and
        charts, calculators and other interactive elements), authority 20 (author,
        dates, recency — under 3 months best, over 6 stale — links to primary sources,
        and the brand on Wikipedia, Wikidata, Reddit, YouTube and LinkedIn from the
        site's sameAs and Wikidata, expert quotes with attribution), technical 20
        (server-side rendering from the crawl, OAI-SearchBot, Claude-SearchBot and
        PerplexityBot allowed, an RSL licence, snippets allowed — nosnippet or
        max-snippet:0 keeps a page out of AI Overviews and AI Mode, data-nosnippet
        reported; llms.txt reported at weight 0). Training, search and user crawlers are
        reported apart, Bytespider, cohere-ai, Google-CloudVertexBot and Google-Agent
        (which ignores robots.txt) among them. Also a readiness score per answer engine
        (Google AI Overviews, AI Mode, ChatGPT, Perplexity, Claude, Bing Copilot) from
        the parts each leans on, 0 where its crawler is blocked: readiness, not measured
        citations. brandMentions: true adds how often Google finds the brand named on
        the web, Reddit, YouTube, LinkedIn and Wikipedia (five paid results pages; quote
        with estimate_cost). Unmeasured parts are null and the rest rescaled; a
        heuristic, and said so. Answers 'are our pages written to be cited by ChatGPT
        and Perplexity' and 'what is our GEO score'. Free without brandMentions. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("get_geo_readiness", _present({"clientId": client_id, "urls": urls, "topPages": top_pages, "brandMentions": brand_mentions, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_goal_report(self, *, client_id: str, goal_ids: Optional[List[str]] = None, by: Optional[Literal["none", "channel", "landing_page", "source", "campaign", "ai_referrer", "query_cluster"]] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Goals by channel, page or query. Visits, converting visits, conversions,
        conversion rate and value for each goal (default every goal), broken down by
        channel, landing page, source, campaign, the AI assistant that referred the
        visit, or the Search Console query cluster bringing people to the landing page.
        Answers 'which channel brings sign-ups', 'what is organic search worth in
        conversions', 'do visits from ChatGPT convert'. Free."""
        return self.call("get_goal_report", _present({"clientId": client_id, "goalIds": goal_ids, "by": by, "days": days, "limit": limit}))

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

    def get_google_trends(self, *, client_id: str, keywords: List[str], time_range: Optional[Literal["past_30_days", "past_90_days", "past_12_months", "past_5_years", "2004_present"]] = None, type_: Optional[Literal["web", "news", "youtube", "images", "froogle"]] = None, worldwide: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Google Trends for up to five keywords. Google Trends interest over time (0–100,
        relative to the busiest point) for up to five keywords compared, by region, and
        — for a single keyword — the related searches, top and rising. Web search by
        default, or news, YouTube, images or shopping. Supersedes get_keyword_trends,
        which reads the United States only. Answers 'is this topic growing', 'when does
        it peak' and 'which of these terms is bigger'. A paid lookup on the client's
        account unless anyone read the same thing this week (spend says which); quote it
        with estimate_cost. (about $0.01) Can spend: pass max_cost_micros to cap it."""
        return self.call("get_google_trends", _present({"clientId": client_id, "keywords": keywords, "timeRange": time_range, "type": type_, "worldwide": worldwide, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_hreflang_parity(self, *, client_id: str, crawl_id: Optional[str] = None, url: Optional[str] = None, source_lang: Optional[str] = None, max_pairs: Optional[int] = None) -> Any:
        """Are the language versions real translations. Reads each language version of the
        client's pages (the groups the crawl's hreflang or /es/-style paths tie
        together) and scores every pair against its source 0–100: equal H2 and H3
        counts; title, meta description and schema inLanguage actually localised (the
        language detected, not just declared); length within the band the language
        should take (German 25–35% longer than English, Japanese 10–25% shorter, in
        words); a stale translation (modified before its source); numbers, dates, prices
        and phone numbers written for the locale; and source-language sentences left
        untranslated. Unmeasured parts are null and the rest rescale. Each pair also
        carries a cultural adaptation check against its market's profile (DACH,
        Francophone, Hispanic, Japanese: formal address, hard-sell CTAs, Impressum or
        Mentions légales, local number, date and currency formats, US brands, statistics
        and laws, length against English), each failure a Medium 'Cultural Adaptation'
        finding, and machine-translation QA (body identical to the source, <html lang>
        against the detected language, a translated meta description over 160
        characters, schema inLanguage, Google's translate widget). contentParity scores
        each group 30/30/25/15: the page exists in every declared language, title, meta
        and schema localised, structure (sections ±1, images and charts exact, FAQ items
        ±2), and freshness (≤7, 8–30, 31–90, 90+ days behind). A heuristic, and it says
        so. url picks the group containing that page; sourceLang which version the
        others are measured against (default the x-default one). Answers 'is our German
        site actually translated' and 'which translations are out of date'. Free:
        fetches the client's own pages."""
        return self.call("get_hreflang_parity", _present({"clientId": client_id, "crawlId": crawl_id, "url": url, "sourceLang": source_lang, "maxPairs": max_pairs}))

    def get_hreflang_report(self, *, client_id: str, crawl_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Hreflang across the site. Validates hreflang as clusters of pages rather than
        page by page, reading it from the pages and from xhtml:link entries in the
        sitemaps (and flagging where the two disagree): return links (a pair Google
        ignores because the other page does not name this one back), x-default, valid
        language-script-region codes (zh-Hant-TW is one; en-uk, es-EU, en-UN and es-LA
        are not; a bare country such as gb or us is not a language), self-reference,
        targets that redirect, error, are noindexed or are canonicalised elsewhere
        (canonical conflicts), hreflang on a page that is itself canonicalised away, and
        pages in a group naming different pages for one language. Answers 'is our
        hreflang set up correctly' and 'why does Google show the wrong language'. Free."""
        return self.call("get_hreflang_report", _present({"clientId": client_id, "crawlId": crawl_id, "limit": limit}))

    def get_image_serp(self, *, client_id: str, keyword: str, location_code: Optional[int] = None, language_code: Optional[str] = None, device: Optional[Literal["desktop", "mobile"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who owns the image results for a keyword. Reads Google's organic results 100
        deep for a keyword and every image pack in them: how many packs and where they
        sit, which domains hold the first ten images (and how dominant the top one is),
        the alt text pattern (how many have alt, average length, the share containing
        the keyword, the commonest words), the format mix (JPEG, WebP, AVIF…) and
        whether the client's site appears in a pack and where it ranks organically.
        Answers 'can we win image results for this', 'who dominates image search here'
        and 'how do the winners write their alt text'. Paid: a results page read 100
        deep, billed per ten results; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_image_serp", _present({"clientId": client_id, "keyword": keyword, "locationCode": location_code, "languageCode": language_code, "device": device, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

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

    def get_integration_connect_link(self, *, client_id: str, provider: Literal["stripe", "shopify", "slack", "linear", "google_sheets", "bigquery"], shop: Optional[str] = None, team_id: Optional[str] = None) -> Any:
        """Link to connect by consent. A link that connects one of the client's accounts by
        signing in rather than pasting a key: Stripe (Connect, read-only), Shopify
        (OAuth; give shop), Slack (installs the app into a channel), Linear (OAuth; give
        teamId), Google Sheets or BigQuery (the client's Google account, with only that
        scope). Valid for ten minutes, for someone signed in to this agency. Answers
        'connect the client's Google Sheets'. Free."""
        return self.call("get_integration_connect_link", _present({"clientId": client_id, "provider": provider, "shop": shop, "teamId": team_id}))

    def get_internal_link_graph(self, *, client_id: str, crawl_id: Optional[str] = None, sort: Optional[Literal["pagerank", "inlinks", "depth"]] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
        """The internal link graph. Every crawled page with its internal inlinks and
        outlinks, clicks from the home page, internal PageRank (0–100), and the anchors
        it is linked with — plus orphans (indexable pages nothing links to), pages
        unreachable from the home page, and pages more than three clicks deep. Links
        that redirect are followed to the page they land on; nofollow links do not
        count. Answers 'which pages are buried', 'what holds our internal authority' and
        'which pages are orphaned'. Free."""
        return self.call("get_internal_link_graph", _present({"clientId": client_id, "crawlId": crawl_id, "sort": sort, "limit": limit, "offset": offset}))

    def get_issue_templates(self, *, client_id: str, crawl_id: Optional[str] = None, rule_id: Optional[str] = None, indexable_only: Optional[bool] = None) -> Any:
        """Issues by template. Groups each issue's pages by URL template (ids, slugs with
        numbers and query values replaced by *), so '62 pages of
        /community/es/u/*?sort=*' reads as one fix on one template. Answers 'how many
        fixes is this really' and 'which template causes this'. ruleId narrows to one
        issue. indexableOnly (default true) leaves out findings on pages search engines
        will not index as themselves — noindexed, not answering 200, or canonicalised
        elsewhere — except the findings that explain why; pass false to see everything.
        Free."""
        return self.call("get_issue_templates", _present({"clientId": client_id, "crawlId": crawl_id, "ruleId": rule_id, "indexableOnly": indexable_only}))

    def get_job(self, *, client_id: str, job_id: str) -> Any:
        """How a slow job is going. One way to follow anything slow — a crawl, a rank or
        domain refresh, a performance run: its status (queued, running, done, failed),
        progress, an ETA where one can be told, and the tool that reads the finished
        result. jobId is kind:id — crawl:<crawlId> (from start_crawl), rank:<runId>
        (refresh_rankings), domain:<runId> (refresh_domain_data), performance:<runId>.
        An AI visibility check reports through get_ai_visibility_runs. Answers 'is my
        crawl done'. Free."""
        return self.call("get_job", _present({"clientId": client_id, "jobId": job_id}))

    def get_keyword_advertisers(self, *, client_id: str, keyword: str, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who advertises on a keyword. The ads Google shows for a keyword right now: each
        advertiser's domain, landing page, headline and description, in order. Answers
        'who bids on this' and 'what do their ads say'. A paid lookup on the client's
        account unless anyone read the same thing recently (spend says which); quote it
        with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_keyword_advertisers", _present({"clientId": client_id, "keyword": keyword, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_keyword_difficulty(self, *, client_id: str, keyword_ids: List[str]) -> Any:
        """Get keyword difficulty. How hard the first page looks for given keywords, scored
        from how many domains link to the pages already ranking there. Answers 'is this
        term worth going after'. Null where too few results have link data to judge."""
        return self.call("get_keyword_difficulty", _present({"clientId": client_id, "keywordIds": keyword_ids}))

    def get_keyword_gap(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get keyword gap. Keywords competitors rank for that the client does not, sized
        by the clicks available — from the client's own tracked captures, so free. For
        any domains and every keyword they rank for, get_domain_keyword_gap reads
        DataForSEO's index. Answers 'which terms are we missing'."""
        return self.call("get_keyword_gap", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_keyword_list(self, *, list_id: str) -> Any:
        """Read a keyword list. Every keyword in one list (by listId from
        list_keyword_lists): the term, its market, language and engine, its keywordId,
        its note and tags, and the metrics last stored for it. Answers 'what is on this
        list'. To filter, sort or export as CSV use query_keyword_list. Free."""
        return self.call("get_keyword_list", _present({"listId": list_id}))

    def get_keyword_metrics(self, *, client_id: str, keywords: List[str], engine: Optional[Literal["google", "bing", "amazon", "youtube"]] = None, location_codes: Optional[List[int]] = None, location_name: Optional[str] = None, language_code: Optional[str] = None, clickstream: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Metrics for a list of keywords. Volume (with 12 months of history), CPC,
        competition, difficulty, intent and SERP features for up to 700 known keywords —
        in one or more countries (locationCodes, up to 5), or a city, county or region
        (locationName, from Google Ads, e.g. 'London,England,United Kingdom'). Countries
        the research index does not cover are answered from Google Ads. clickstream:
        true adds clickstream-refined volume (twice the cost). engine bing gives Bing's
        volume, CPC, competition and history from Bing Ads (English, French and German);
        engine amazon gives Amazon search volume from DataForSEO Labs (volume only).
        YouTube publishes no volume and is refused with that reason. Answers 'what is
        the volume of these keywords', 'how many people search this in Madrid' and 'how
        often is this searched on Bing or Amazon'. A paid lookup on the client's account
        unless anyone read the same thing recently (spend says which); quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_keyword_metrics", _present({"clientId": client_id, "engine": engine, "keywords": keywords, "locationCodes": location_codes, "locationName": location_name, "languageCode": language_code, "clickstream": clickstream, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_keyword_trends(self, *, client_id: str, terms: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Get Google Trends interest for terms. Interest over time from Google Trends for
        up to five terms in the United States, each on a 0–100 scale relative to its own
        peak — so it shows when people care, not how many. Kept for existing callers;
        get_google_trends does the same for any market or worldwide, with regions,
        rising searches and news, YouTube, image or shopping search, and is the one to
        use. Answers 'is this seasonal' and 'is this growing'. Different from
        get_search_demand, which counts people in our own panel. A paid lookup on the
        client's account: quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_keyword_trends", _present({"clientId": client_id, "terms": terms, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_landing_pages(self, *, client_id: str, tracker_id: str) -> Any:
        """Which pages the tracked keywords land on. For a rank tracker's latest captures:
        each of the client's pages with how many tracked keywords it ranks for, how many
        in the top 3 and top 10, its average position and best keyword — and the
        keywords where two or more of its pages compete. Answers 'which pages carry our
        rankings' and 'where are we cannibalising'. Free."""
        return self.call("get_landing_pages", _present({"clientId": client_id, "trackerId": tracker_id}))

    def get_link_checks(self, *, client_id: str) -> Any:
        """Do the linking pages still link?. What our own crawler last saw on each page
        said to link to the client: live (the link is there), lost (the page no longer
        links), unknown (the page could not be read), moved (the page redirected
        elsewhere and the link is not at the new address, with movedTo) or
        unverifiable_js (the page is a JavaScript app shell, so its links cannot be seen
        without a browser), with counts, and rendered: true where the last check read
        the page in a browser. Only lost is a removal. Read from the last check, never
        fetched now. Answers 'which links have we lost'. Run recheck_links to check
        again, or recheck_links with render: true to read the unverifiable_js pages in a
        browser. Free."""
        return self.call("get_link_checks", _present({"clientId": client_id}))

    def get_link_gap(self, *, client_id: str, competitors: List[str], target: Optional[str] = None, match: Optional[Literal["any", "all"]] = None, limit: Optional[int] = None, source: Optional[Literal["auto", "vendor", "index"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Link gap against competitors. The sites that link to competitors but not to the
        client — match any: at least one competitor (one read each); match all: every
        competitor (one read) — with each site's rank and how many links it sends each
        competitor. The outreach list Ahrefs calls Link Intersect, for any domains.
        Answers 'who links to them and not to us'. source index answers free from our
        own link index (page-level links and Common Crawl's domain graph; rank is null
        there); auto uses it when it holds every domain involved (50+ links each, or a
        complete graph pass) and otherwise asks DataForSEO; vendor always asks
        DataForSEO. source says which answered. Vendor reads: A paid lookup on the
        client's account unless anyone read the same thing this week (spend says which);
        quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_link_gap", _present({"clientId": client_id, "target": target, "competitors": competitors, "match": match, "limit": limit, "source": source, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_link_intersect(self, *, client_id: str, competitor_domains: List[str]) -> Any:
        """Get link prospects. Sites linking to the client's competitors but not to the
        client. Answers 'who should we approach for links'."""
        return self.call("get_link_intersect", _present({"clientId": client_id, "competitorDomains": competitor_domains}))

    def get_link_velocity(self, *, client_id: str, domains: Optional[List[str]] = None, days: Optional[int] = None, baseline_days: Optional[int] = None, grace_days: Optional[int] = None) -> Any:
        """Referring domains gained and lost per day. New and lost referring domains per
        day for the client and its tracked competitors (or the domains given), from our
        own link index and the vendor links already synced, each against the domain's
        own baseline of the preceding weeks: spikes (a day of new referring domains far
        above its usual — a campaign, a viral piece, or somebody pointing a link farm at
        the site) and lost clusters (many domains lost on one day — a network deindexed,
        a partner's redesign, a broken migration), with example domains, and five red
        flags with the action each calls for (10× the usual new links in a week, half
        the links lost in a month, no new links for three months, every new link from
        one TLD, a spike from one country). Losses are only called after graceDays
        unseen, and not at all for a domain no index is still reading. Answers 'are we
        gaining links faster than usual', 'did we just lose a batch of links' and 'is a
        competitor running a link campaign'. Free."""
        return self.call("get_link_velocity", _present({"clientId": client_id, "domains": domains, "days": days, "baselineDays": baseline_days, "graceDays": grace_days}))

    def get_live_serps(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None, engine: Optional[Literal["google", "bing", "youtube", "amazon", "yandex", "baidu", "naver", "duckduckgo", "yahoo", "seznam", "app_store", "google_play"]] = None, device: Optional[Literal["desktop", "mobile"]] = None, top: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Read several results pages now. Reads the live results page for up to 10
        keywords in one market and engine (Google by default), and returns each page's
        top results (position, type, domain, url, title) and the search features on it.
        Answers 'who ranks for these right now'. Each keyword is one purchase, made in
        turn; one that fails is reported and the rest still return; maxCostMicros stops
        before the purchase that would pass it. Quote with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_live_serps", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "engine": engine, "device": device, "top": top, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_llm_responses(self, *, client_id: str, prompt: str, platforms: Optional[List[Literal["chat_gpt", "chat_gpt_app", "claude", "gemini", "perplexity"]]] = None, web_search: Optional[bool] = None, country: Optional[str] = None, models: Optional[Dict[str, Any]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Ask ChatGPT, Claude, Gemini and Perplexity through DataForSEO. Asks one question
        (up to 500 characters) live on the chosen models through DataForSEO — chat_gpt,
        claude, gemini, perplexity, and chat_gpt_app: the ChatGPT app itself as a person
        sees it, with the sources it cited and the searches it ran (about $0.004) — with
        web search on by default, and returns each answer's text, the pages it cited,
        the follow-up searches it ran (fanOutQueries, where the platform reports them),
        and which of the client's tracked brands it named and whether the client was
        named and cited. Needs no assistant keys of the agency's own; nothing is stored.
        Use it to explore a question before tracking it. Answers 'what do the big models
        say when asked this' and 'what does ChatGPT search for to answer it'. A paid
        lookup on the client's account unless anyone asked the same thing recently
        (served says which); quote it with estimate_cost. (one purchase per model; about
        $0.01–0.10 each with web search) Can spend: pass max_cost_micros to cap it."""
        return self.call("get_llm_responses", _present({"clientId": client_id, "prompt": prompt, "platforms": platforms, "webSearch": web_search, "country": country, "models": models, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_local_categories(self, *, client_id: str, lat: float, lng: float, radius_km: Optional[float] = None, categories: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Business categories in an area. The Google business categories used around a
        point, with how many businesses use each, and the attributes common among them —
        the categories a listing should name, and the gaps. Narrow it with categories to
        see what businesses in those also list. Answers 'which secondary categories do
        the dentists here use'. A paid lookup on the client's account unless anyone read
        the same thing recently; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_local_categories", _present({"clientId": client_id, "lat": lat, "lng": lng, "radiusKm": radius_km, "categories": categories, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_local_seo_audit(self, *, client_id: str, location_id: str, use_listing: Optional[bool] = None, posts_task_id: Optional[str] = None, competitor_radius_km: Optional[float] = None, directories: Optional[bool] = None, duplicates: Optional[bool] = None, city: Optional[str] = None, service: Optional[str] = None, model: Optional[Literal["auto", "storefront", "sab", "hybrid"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Local SEO audit of a location. Scores one location's local SEO 0–100 (a
        heuristic, said so in the answer) from six weighted parts, each check full,
        partial or low with the reason, or null when not measured — then left out and
        the other weights rescaled: the Google Business Profile (25: primary category
        against the homepage, about four secondary categories, posts, photos, Q&A,
        hours), reviews (20: at least 10, the rating, the last three months, six months'
        monthly flow and gaps over three weeks, owner response rate, and a fake-review
        flag when two of six patterns match), the site (20: city and service in the
        title and H1, visible NAP, a tel: link, a map embed, location pages over 60%
        unique by the city-swap test, gates at 30 and 50 location pages), NAP and
        citations (15, the check_nap_consistency comparison; directories: true adds the
        directory citations), LocalBusiness schema (10: a subtype, geo to five decimals,
        priceRange under 100 characters, a unique @id per location with branchOf) and
        links (10); plus a rating spread that leans to five stars, review gating,
        service pages, location pages within three clicks, hours on the site, trust
        badges, the PostalAddress parts, the subtype that fits the vertical, areaServed,
        retired VehicleListing and SpecialAnnouncement markup and, with duplicates,
        other listings at the same address or phone. gbpChecklist scores the 25-field
        profile checklist (2/1/0 per field, null where DataForSEO returns nothing —
        verified status, Q&A, videos, products, photo dates — weighted by vertical,
        banded 90/75/50/25); grid reads back the latest grid scan for the main service
        (share of local voice, visibility points, the worst quadrant, a heatmap);
        mapsHealth combines profile 25, grid 20, reviews 20, NAP 15, schema 10 and rival
        standing 10. Detects storefront, service-area business (which skips the map and
        address checks) or hybrid, and the vertical; adds listing completeness 0–100
        and, with competitorRadiusKm, the competitors per km² in the primary category.
        Reviews come from sync_local_reviews; posts from a get_business_posts task
        passed as postsTaskId. Answers 'how good is our local SEO' and 'what should we
        fix first for the map pack'. useListing reads the live listing and its Q&A, and
        competitorRadiusKm one business search, all paid: quote with estimate_cost. Free
        with useListing false and competitorRadiusKm 0. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_local_seo_audit", _present({"clientId": client_id, "locationId": location_id, "useListing": use_listing, "postsTaskId": posts_task_id, "competitorRadiusKm": competitor_radius_km, "directories": directories, "duplicates": duplicates, "city": city, "service": service, "model": model, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_local_visibility(self, *, client_id: str, location_id: str, term: str) -> Any:
        """Map-pack visibility and reviews for a location. The latest grid scan for a
        search term at one location — the map-pack position at every point, and the
        share of points ranking in the top 3 and top 10, a summary (share of local voice
        with its band — dominant 80+, strong 60+, moderate 40+, weak 20+, critical —
        visibility points 3 for the top three and 1 for fourth to tenth, each compass
        quadrant and the worst, and the grid as rows north to south for a heatmap, with
        a text version), and a competitor table: every business the grid saw, with its
        share of local voice (the share of points where it holds a top-3 slot), points
        seen, average position, rating and reviews — plus an analysis of the location's
        reviews (rating, volume, recency, response rate). Answers 'where in town do we
        show up for this search'. scanned is false when that term has never been scanned
        there: no grid, rather than a grid of blanks that would read as invisible
        everywhere. Free."""
        return self.call("get_local_visibility", _present({"clientId": client_id, "locationId": location_id, "term": term}))

    def get_log_orphans(self, *, client_id: str, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Pages crawlers find that the audit does not. Pages search and AI crawlers
        fetched successfully in the connected logs that the latest site crawl never
        reached — nothing on the site links to them, yet they are crawled (old
        campaigns, forgotten sections, pages only a sitemap or another site names) —
        with hits, which crawlers and when last seen. Answers 'which orphan pages is
        Google still crawling'. Free."""
        return self.call("get_log_orphans", _present({"clientId": client_id, "days": days, "limit": limit}))

    def get_long_tail_candidates(self, *, client_id: str, days: Optional[int] = None, min_impressions: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Queries with impressions and no page of their own. Search Console queries the
        site is shown for where the page Google picked is about something else — its
        title and H1 (from the latest crawl) cover under half the query's words —
        clustered by shared words into write candidates, biggest first, each with its
        queries, impressions and the pages ranking now (where to link the new page
        from). Branded queries are left out. Answers 'what should we write next' and
        'which searches have no page'. Free."""
        return self.call("get_long_tail_candidates", _present({"clientId": client_id, "days": days, "minImpressions": min_impressions, "limit": limit}))

    def get_low_ctr_queries(self, *, client_id: str, days: Optional[int] = None, min_impressions: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Queries losing clicks to their snippet. Search Console queries on page one
        (positions 1–10) with enough impressions where far fewer people click than that
        position normally earns (under half the click curve's rate): actual and expected
        click-through rate and the clicks missed, worst first. Answers 'which titles and
        descriptions should we rewrite'. Check get_serp_features first — an AI overview
        or map pack above the result also lowers clicks. Free."""
        return self.call("get_low_ctr_queries", _present({"clientId": client_id, "days": days, "minImpressions": min_impressions, "limit": limit}))

    def get_maps_results(self, *, client_id: str, keyword: str, surface: Optional[Literal["maps", "local_finder"]] = None, zoom: Optional[int] = None, depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, lat: Optional[float] = None, lng: Optional[float] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Google Maps results from one spot. The Google Maps (or Local Finder) results for
        a keyword as searched from one point — or the client's country — with every
        business's rating, reviews, category, site and ids, and where the client sits.
        One lookup, where a grid scan is many. Answers 'who shows on the map for this
        from downtown'. A paid lookup on the client's account unless anyone read the
        same thing recently; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_maps_results", _present({"clientId": client_id, "keyword": keyword, "surface": surface, "zoom": zoom, "depth": depth, "locationCode": location_code, "languageCode": language_code, "lat": lat, "lng": lng, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_matomo_report(self, *, client_id: str, report: Optional[Literal["overview", "channels", "landing_pages", "pages", "goals"]] = None, channel: Optional[Literal["all", "organic", "ai"]] = None, from_: Optional[str] = None, to: Optional[str] = None, compare: Optional[bool] = None, limit: Optional[int] = None) -> Any:
        """Visits, pages and goals (Matomo). For a client that measures with Matomo instead
        of GA4, read live from their Matomo. report: overview (visits, unique visitors
        when the server processes them for ranges, actions, pageviews, bounce rate,
        average time, conversions, conversion rate, revenue); channels (visits, bounce
        rate, conversions and revenue by referrer channel: search, social, ai, direct,
        website, campaign — Matomo's own split); landing_pages (entrances, bounce rate,
        actions per entrance, conversions and revenue credited to the entry page); pages
        (pageviews, visits, average time, bounce and exit rate by page URL); goals
        (conversions, conversion rate and revenue per goal, and in total). channel
        limits overview, landing_pages, pages and goals to search engines (organic) or
        AI assistants (ai) through a Matomo segment; Matomo answers a segment only once
        it has processed it, and says so. Compares with the same number of days before
        unless compare is false; defaults to the 28 days ending yesterday. Rows carry
        key, label, current and previous (null where that period had no row). Figures
        Matomo did not send are null, never zero. Refuses with a sentence when Matomo is
        not connected (connect_integration with provider matomo). Answers 'is organic
        traffic growing' and 'which landing pages convert' for a Matomo site. Free."""
        return self.call("get_matomo_report", _present({"clientId": client_id, "report": report, "channel": channel, "from": from_, "to": to, "compare": compare, "limit": limit}))

    def get_media_report(self, *, client_id: str, crawl_id: Optional[str] = None, check_sizes: Optional[bool] = None) -> Any:
        """Images and video. Images and video across a crawl: alt text coverage, formats
        (and the share in AVIF or WebP), pages whose first image — usually the Largest
        Contentful Paint element — is lazy-loaded, how many images the image sitemap
        lists, embedded video with and without VideoObject markup and video sitemap
        coverage, plus the image checks' page counts. checkSizes asks the server for up
        to 100 image sizes (HEAD requests to the client's own hosts and its image CDNs)
        and lists the heaviest, with each judged against its role's band (thumbnail:
        target under 50KB, warn over 100KB, critical over 200KB; content: 100/200/500KB;
        hero, the page's first image: 200/300/700KB), and reads up to 20 product images'
        XMP for an IPTC DigitalSourceType that declares them AI-generated
        (trainedAlgorithmicMedia, compositeSynthetic, algorithmicMedia,
        compositeWithTrainedAlgorithmicMedia), and grades each image's browser caching
        (cache: long at a max-age of a week or more or immutable, short under a week,
        none with no-store, no-cache or no lifetime at all). Always: image hosts and the
        CDN each shows (by name, or by response headers when sizes are checked), the
        share on a separate host, and how pages lazy-load (native, perfmatters, EWWW, a
        generic script loader or none; script loaders are not reported as missing lazy
        loading). Answers 'are our images slowing the site down', 'which images lack alt
        text' and 'can our videos show in video results'. Free."""
        return self.call("get_media_report", _present({"clientId": client_id, "crawlId": crawl_id, "checkSizes": check_sizes}))

    def get_naver_keyword_volumes(self, *, client_id: str, keywords: List[str], include_related: Optional[bool] = None) -> Any:
        """Naver's own search volume. Monthly searches on Naver, PC and mobile, from the
        keyword tool in the agency's Naver Search Ad account, for up to 50 terms, with
        Naver's related terms when includeRelated is true. The only source of Naver
        demand: no vendor resells it. Terms too rare are reported by Naver as under ten
        and flagged so, not given a number. Answers 'how often is this searched on
        Naver'. Free; needs the agency's Naver Search Ad credentials."""
        return self.call("get_naver_keyword_volumes", _present({"clientId": client_id, "keywords": keywords, "includeRelated": include_related}))

    def get_next_steps(self, *, client_id: str) -> Any:
        """What to do next for a site. Answers 'what is left to do for this site, and what
        call does it'. The onboarding checklist with live status — done, todo, in
        progress, failed or blocked and why — each with the exact tool and arguments to
        call next; then the optional connections that unlock more tools (Bing Webmaster
        key, PageSpeed / Chrome UX Report key, alert delivery, rank tracker keywords, AI
        visibility schedule, analytics goals, crawl schedule), each with its status and
        call; then, once the site is set up, the weekly loop's calls with their
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

    def get_outbound_domains(self, *, client_id: str, domain: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Domains a site links out to. The domains a site (the client's or any other)
        links out to, with how many links, how many of them dofollow and the dofollow
        share, and from how many of its pages. A site that already links to your
        competitors is an outreach prospect; one linking to dead or spammy domains is a
        risk. Read from our own crawl of the site; when we have not crawled it, its
        homepage and up to 15 pages it links to are fetched now. Free. Answers 'who does
        this site link to' and 'which resources does this niche cite'."""
        return self.call("get_outbound_domains", _present({"clientId": client_id, "domain": domain, "limit": limit}))

    def get_outreach_mailboxes(self, *, client_id: str) -> Any:
        """Mailboxes outreach is sent from. The Gmail and Microsoft 365 mailboxes connected
        for the client's outreach, with when replies were last checked and any error,
        and the links where a person connects another (they sign in themselves; nothing
        here can). Answers 'which mailbox do we send from' and 'is outreach email
        working'. Free."""
        return self.call("get_outreach_mailboxes", _present({"clientId": client_id}))

    def get_outreach_status(self, *, client_id: str) -> Any:
        """Where each outreach conversation stands. Every prospect the client has written
        to, with its stage, contact, when it replied, and each email of its sequence:
        sent, scheduled, failed or called off. Answers 'who have we emailed', 'who
        replied' and 'what is going out this week'. Free."""
        return self.call("get_outreach_status", _present({"clientId": client_id}))

    def get_page_backlinks(self, *, client_id: str, url: str, dofollow_only: Optional[bool] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who links to one page. The sites linking to one exact page — one row per linking
        domain, live links only, best domains first — with the linking page, its title,
        the anchor, dofollow and the domain's rank. Run it on a competitor's dead page
        from get_competitor_broken_pages to get the people to write to (broken-link
        building), or on any page to see who cites it. Answers 'who links to that dead
        page' and 'who would link to ours instead'. A paid DataForSEO read unless anyone
        read the same page this week; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_page_backlinks", _present({"clientId": client_id, "url": url, "dofollowOnly": dofollow_only, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_page_details(self, *, client_id: str, url: str, crawl_id: Optional[str] = None) -> Any:
        """Everything the crawl read on a page. One crawled page in full: its H2/H3
        outline, word count, published and modified dates, structured data as written,
        custom extraction values, the addresses that redirect to it, what JavaScript
        changed when it was rendered, and its place in the link graph (inlinks,
        outlinks, click depth, internal PageRank, anchors). Answers 'what does the
        crawler see on this page'. Use get_page_issues for its issues. Free."""
        return self.call("get_page_details", _present({"clientId": client_id, "crawlId": crawl_id, "url": url}))

    def get_page_indexing_reasons(self, *, client_id: str, template: Optional[str] = None, reason: Optional[Literal["indexed", "noindex", "blocked_by_robots", "not_found", "server_error", "redirect", "soft_404", "access_denied", "canonical_elsewhere", "duplicate_without_canonical", "crawled_not_indexed", "discovered_not_indexed", "unknown_to_google", "inspection_failed", "not_inspected", "other"]] = None, limit: Optional[int] = None) -> Any:
        """Why pages are not indexed. Search Console's Page indexing report, rebuilt (its
        API has none): every sitemap and crawled page with one reason it is or is not in
        Google — noindex, blocked by robots.txt, 404, server error, redirect, soft 404,
        Google chose another canonical, crawled or discovered but not indexed, unknown
        to Google — from URL Inspection (2,000 a day per property, worked through the
        sitemap a batch a day) and our crawl, which stands in, marked, for pages not
        inspected yet. Rolled up per template (path pattern) with the share indexed and
        the main reason, and a fix for each reason. Filter by template or reason.
        Answers 'why isn't this page indexed' and 'which templates are kept out of
        Google'. Free."""
        return self.call("get_page_indexing_reasons", _present({"clientId": client_id, "template": template, "reason": reason, "limit": limit}))

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

    def get_parameter_report(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """URL parameters and crawl waste. Every query parameter the crawl met — sort
        orders, filters, tracking, pagination — with how many pages carry it, how many
        of those are canonicalised to another page (crawl waste), their issues, and
        whether to strip it from crawls (set_crawl_settings stripParams), keep it, or
        review it. Answers 'why is the crawl full of ?sort= pages'. Free."""
        return self.call("get_parameter_report", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_parasite_risk(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """Sections that read like rented-out pages. Site reputation abuse risk per section
        (first path segment) from the crawl's text and links: sponsored or partner
        phrases per page (1.0 or more is high risk), commerce phrases per page (2.0 or
        more), outbound links with affiliate parameters such as tag=, aff_id= or ref_=
        per page (3.0 or more), commerce and affiliate together (high risk), and a
        section whose commerce rate is more than twice the site's mean (drift — a
        section that has turned into something else). Each section with its rates,
        signals, risk and the worst pages. A heuristic, labelled as one. Answers 'is any
        part of our site at risk under Google's site reputation abuse policy' and 'which
        section has been turned into coupon or affiliate pages'. Free."""
        return self.call("get_parasite_risk", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_personal_keyword_difficulty(self, *, client_id: str, keywords: List[str], location_code: Optional[int] = None, language_code: Optional[str] = None) -> Any:
        """How hard a keyword is for this site. Keyword difficulty adjusted for the
        client's own site: its authority against the first page's, how much of the topic
        it already ranks for, and whether it already ranks for the keyword — each
        adjustment returned with its reason, so the number can be argued with. Answers
        'which of these can we actually win'. Free: read from stored first pages, link
        counts, authority and rankings; a factor with no data behind it is left out and
        said so."""
        return self.call("get_personal_keyword_difficulty", _present({"clientId": client_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code}))

    def get_platform_reviews(self, *, client_id: str, platform: Literal["tripadvisor", "trustpilot"], business: Optional[str] = None, task_id: Optional[str] = None, depth: Optional[int] = None, location_code: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A business's Tripadvisor or Trustpilot reviews. Reviews of a business on
        Tripadvisor (business: its name and town, or a Tripadvisor URL path such as
        /Restaurant_Review-g…) or Trustpilot (business: its domain), newest first, with
        the platform's own rating and review count, the star spread over the reviews
        read, the average and the owner's response rate — for the cross-platform
        comparison beside Google's reviews (get_business_reviews, sync_local_reviews).
        Both are queued: the first call (with business) is the paid one and returns a
        taskId; calling again with the taskId collects it for free (status pending until
        ready). Answers 'how are we rated on Tripadvisor' and 'what does Trustpilot say
        about this competitor'. A paid lookup on the client's account unless anyone read
        the same thing recently; quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_platform_reviews", _present({"clientId": client_id, "platform": platform, "business": business, "taskId": task_id, "depth": depth, "locationCode": location_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_portfolio_metrics(self, *, portfolio_id: str) -> Any:
        """A portfolio's figures. Traffic, rankings, issues and AI visibility across a
        portfolio, with each member's own row: Google clicks over the newest 28 days and
        the 28 before, tracked keywords in the top 3 and 10 and the average position,
        site health and critical issues from the newest crawl, and how often AI
        assistants named the brand. Each total says how many members it covers; a member
        without the data is left out, never counted as zero. A site member is read for
        that site; AI visibility is per client. Answers 'how are the dental practices
        doing'. Free."""
        return self.call("get_portfolio_metrics", _present({"portfolioId": portfolio_id}))

    def get_position_distribution(self, *, client_id: str, tracker_id: str, days: Optional[int] = None, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get position distribution. How a tracker's keywords spread across positions 1-3,
        4-10, 11-20, 21-50 and 51-100 each day, with average position and visibility,
        per device. Answers 'how many keywords are on page one, and is that growing'.
        Keywords read and not found are counted as not ranking, apart from every band;
        keywords not read that day are counted as not captured. The average is over
        ranking keywords only."""
        return self.call("get_position_distribution", _present({"clientId": client_id, "trackerId": tracker_id, "days": days, "device": device}))

    def get_preload_readiness(self, *, client_id: str, url: Optional[str] = None) -> Any:
        """How ready a page is for instant navigation. A 0–100 heuristic from one page's
        markup and headers, 25 points each: speculation rules (a <script
        type="speculationrules"> block or a Speculation-Rules header) for the next
        navigation; fetchpriority="high" on the image that is probably the Largest
        Contentful Paint; nothing that keeps it out of the back/forward cache
        (Cache-Control: no-store, an unload listener); and no deprecated <link
        rel="prerender">. With what to change for each part missed. A static reading,
        not a measurement: lab diagnostics come from page_lab. url defaults to the
        homepage and must be on the client's site. Answers 'can the next page load
        instantly' and 'why does Back reload the page'. Free."""
        return self.call("get_preload_readiness", _present({"clientId": client_id, "url": url}))

    def get_price_list(self) -> Any:
        """What everything costs. Every paid data operation with its most-per-request price
        in micro-USD and how long an answer stays free once anyone has bought it (the
        shared archive), plus which tools spend. A tool's own quote for given arguments
        is estimate_cost, or the tool itself with dryRun: true. Answers 'how much does
        this cost' and 'what is cached for how long'. Free."""
        return self.call("get_price_list", {})

    def get_query_intents(self, *, client_id: str, days: Optional[int] = None, by: Optional[Literal["intent", "topic"]] = None, brand: Optional[Literal["all", "branded", "non_branded"]] = None, limit: Optional[int] = None) -> Any:
        """Search traffic by intent or topic. Google web clicks, impressions and position
        grouped by what each Search Console query asks for — informational, commercial,
        transactional or navigational (navigational: it names the client, from the
        brief's brand terms) — or by topic (queries sharing their most common words).
        Every query is tagged after each Search Console sync; query_data can also group
        or filter by intent, topic and branded. Answers 'how much of our traffic is
        people ready to buy' and 'which topics bring the clicks'. Free."""
        return self.call("get_query_intents", _present({"clientId": client_id, "days": days, "by": by, "brand": brand, "limit": limit}))

    def get_query_page_swaps(self, *, client_id: str, days: Optional[int] = None, compare: Optional[Literal["previous", "year"]] = None, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, brand: Optional[Literal["all", "branded", "non_branded"]] = None, min_impressions: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Queries answered by a different page. Queries where Google now sends searchers
        to a different page of the site than in the previous period, with both pages and
        their clicks. Answers 'is Google confused about which page to rank' — a swap is
        usually two pages competing (merge them or fix internal links) or a new page
        taking over. Every Search Console query, not only tracked keywords
        (get_url_swaps covers those). Each swap names the registry's owner for the query
        and whether Google's current page is it. searchType picks web (default), image,
        video or news. Free."""
        return self.call("get_query_page_swaps", _present({"clientId": client_id, "days": days, "compare": compare, "searchType": search_type, "brand": brand, "minImpressions": min_impressions, "limit": limit}))

    def get_questions(self, *, client_id: str, days: Optional[int] = None, status: Optional[Literal["all", "unanswered", "answered", "mentioned"]] = None, limit: Optional[int] = None) -> Any:
        """The questions people ask, from every source. Questions about the client's
        subject merged from People Also Ask and related searches on captured results
        pages, the client's AI visibility prompts, Reddit and Quora threads ranking for
        tracked keywords, Search Console queries phrased as questions, and the site's
        own search box (GA4) — phrasings of one question deduplicated — each with its
        sources, volume where a source measured it (impressions, site searches, or
        volume, kept apart) and whether a page of the site answers it: answered (a
        heading asks or states it), mentioned (the text has its words) or unanswered,
        from the latest crawl. sources says which could be read. Answers 'what should
        our FAQ cover' and 'which questions have no page'. Free."""
        return self.call("get_questions", _present({"clientId": client_id, "days": days, "status": status, "limit": limit}))

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

    def get_ranked_keywords(self, *, client_id: str, engine: Optional[Literal["google", "amazon", "app_store", "google_play"]] = None, target: Optional[str] = None, scope: Optional[Literal["auto", "domain", "subdomains", "subfolder", "url"]] = None, paid: Optional[bool] = None, result_type: Optional[Literal["organic", "paid", "ai_overview_reference", "featured_snippet", "local_pack"]] = None, change: Optional[Literal["all", "new", "up", "down", "lost"]] = None, min_position: Optional[int] = None, max_position: Optional[int] = None, min_volume: Optional[int] = None, intent: Optional[Literal["informational", "navigational", "commercial", "transactional"]] = None, contains: Optional[str] = None, sort: Optional[Literal["traffic", "volume", "position", "change"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What a domain ranks for. Every keyword a domain, subfolder or page ranks for in
        Google — position (and the one before), URL, estimated traffic, volume, CPC,
        difficulty, intent and SERP features — filtered and sorted, paginated. paid:
        true (or resultType paid) lists the keywords it buys ads on, with the ad;
        resultType ai_overview_reference lists the keywords whose AI Overview cites it,
        featured_snippet those where it holds the snippet. change new / up / down lists
        its recent ranking movements, and lost the keywords it no longer ranks for (with
        the position it last held). engine amazon reads the keywords an Amazon product
        ranks for (target its ASIN); engine app_store or google_play the keywords an app
        ranks for (target the numeric App Store id or the Play package name; US English
        only) — position, volume and the listing, without the Google-only fields,
        filters or change. Answers 'what does this competitor rank for', 'which keywords
        drive their traffic', 'what did they just start ranking for' and 'which searches
        find this product or app'. A paid lookup on the client's account unless anyone
        read the same thing recently (spend says which); quote it with estimate_cost.
        Can spend: pass max_cost_micros to cap it."""
        return self.call("get_ranked_keywords", _present({"clientId": client_id, "engine": engine, "target": target, "scope": scope, "paid": paid, "resultType": result_type, "change": change, "minPosition": min_position, "maxPosition": max_position, "minVolume": min_volume, "intent": intent, "contains": contains, "sort": sort, "limit": limit, "offset": offset, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_recipe(self, *, client_id: str, name: Optional[Literal["weekly_review", "new_article", "technical_audit", "site_migration", "competitor_teardown", "ai_visibility_baseline"]] = None) -> Any:
        """A named plan of calls. An ordered call plan for a common job, with arguments
        filled in from the client (its domain, rivals, a keyword it ranks for) and the
        ones left to fill named in fill. Recipes: weekly_review, new_article,
        technical_audit, site_migration, competitor_teardown, ai_visibility_baseline. A
        plan, not automation: make each call, read it, and skip a step the one before
        says is unnecessary. With no name, lists them. Answers 'what's the process for a
        technical audit'. Free."""
        return self.call("get_recipe", _present({"clientId": client_id, "name": name}))

    def get_referring_domains(self, *, client_id: str, domain: Optional[str] = None, source: Optional[Literal["auto", "vendor", "index"]] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Referring domains. The domains linking to a domain (the client's or any
        competitor's), with how many links each sends, whether they follow, the linking
        domain's authority (0–100) and when the links were first and last seen. Answers
        'who links to us', 'who links to them' and 'which sites are worth asking'.
        source index is free: our own link index (our crawls, client crawls' outlinks,
        Common Crawl, Bing). auto answers from the index when it holds 50+ links to the
        domain (or, for referring domains, a complete pass of Common Crawl's domain
        graph), and otherwise asks the vendor — a paid lookup on the client's account
        unless anyone bought it in the last week; coverage says which answered. vendor
        always asks the vendor. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_referring_domains", _present({"clientId": client_id, "domain": domain, "source": source, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_referring_networks(self, *, client_id: str, target: Optional[str] = None, type_: Optional[Literal["ip", "subnet"]] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Which networks the links come from. The IP addresses or subnets (type ip or
        subnet) the client's links — or any target's — come from, from DataForSEO's
        referring networks: per network its backlinks, referring domains and main
        domains, rank, first seen and lost date, with the networks carrying links from
        five or more separate domains flagged. Many unrelated sites on one address is
        the shape of a private blog network; a shared host puts honest sites together
        too, so a flag means look at the sites, not disavow. Answers 'are our links from
        a link network' and 'how many of these sites share a server'. One paid
        DataForSEO request; quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("get_referring_networks", _present({"clientId": client_id, "target": target, "type": type_, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_rendering_report(self, *, client_id: str, crawl_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """What JavaScript changes. Pages the crawl rendered with JavaScript, compared with
        their raw HTML: words and links that exist only after JavaScript runs, and a
        title, canonical, meta robots, H1, description or structured data that
        JavaScript changes — what a search engine or an AI crawler that does not run
        scripts never sees. Answers 'does our content depend on JavaScript'. Turn
        rendering on with set_crawl_settings render. Free."""
        return self.call("get_rendering_report", _present({"clientId": client_id, "crawlId": crawl_id, "limit": limit}))

    def get_report_data(self, *, client_id: str, from_: str, to: str, compare_to: Optional[Literal["previous_period", "previous_year"]] = None) -> Any:
        """Every figure a monthly report needs. One read of a client's period, from..to
        inclusive, against the period before (compareTo previous_period, the default) or
        the same days a year earlier (previous_year): searchConsole (clicks,
        impressions, CTR and position in total, branded and non-branded, with the
        non-branded queries and pages that moved most), analytics (GA4 organic sessions,
        key events and revenue, or the first-party web analytics' visits), revenue
        (imported orders by currency, organic and AI channels, attribution coverage — as
        get_seo_revenue), rankings (each tracker's summary and movers between the
        period's ends), audit (the latest crawl in the period, its health, and new and
        fixed issues against the last crawl before it), backlinks (gained and lost),
        aiVisibility (mention rate against the comparison), annotations (the timeline,
        with Google's updates) and alerts fired. A section is null with
        unavailableReason when the client lacks that source. Answers 'pull October's
        numbers for the report'. Use it first; the single tools go deeper on one
        section. Free."""
        return self.call("get_report_data", _present({"clientId": client_id, "from": from_, "to": to, "compareTo": compare_to}))

    def get_robots_history(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """How robots.txt and the sitemaps changed. The robots.txt each crawl read, newest
        first, with the lines added and removed against the version before (a new
        Disallow, a dropped Sitemap line), and per crawl how many sitemaps and entries
        were listed. Answers 'who changed robots.txt and when', 'why did Google stop
        crawling /blog' and 'did the sitemap shrink'. Free."""
        return self.call("get_robots_history", _present({"clientId": client_id, "limit": limit}))

    def get_run_status(self, *, client_id: str, job: Literal["rank", "domain", "links"], run_id: str) -> Any:
        """Get the status of a run. How a run started with refresh_rankings (job 'rank'),
        refresh_domain_data (job 'domain') or recheck_links (job 'links', including a
        browser re-check with render) is going: running, done or failed, and — when it
        failed or captured only some keywords — the reason, written for an agency to act
        on (a missing vendor key, an unreachable site). Answers 'did that capture work'.
        A run id that is not this client's, or that has aged out, reads as unknown."""
        return self.call("get_run_status", _present({"clientId": client_id, "job": job, "runId": run_id}))

    def get_search_anomalies(self, *, client_id: str, lookback_days: Optional[int] = None, scopes: Optional[List[Literal["site", "section", "topic"]]] = None) -> Any:
        """Unusual days in search traffic, explained. Days when Google clicks fell or
        jumped well outside their normal range — for the whole site, each section (first
        path segment) and each query topic — against a robust same-weekday baseline
        (median and MAD over eight weeks), consecutive days joined into one episode.
        Each names the likely cause from the timeline with a confidence: a crawl
        regression (pages gone 404 or newly noindex), a deploy or crawl change, a Google
        update, a lost SERP feature, or a page swap (the ranking URL changed). Also
        lists what the daily check already raised. Answers 'why did traffic drop on
        Tuesday' and 'is anything wrong with search'. Free."""
        return self.call("get_search_anomalies", _present({"clientId": client_id, "lookbackDays": lookback_days, "scopes": scopes}))

    def get_search_appearance(self, *, client_id: str, days: Optional[int] = None, compare: Optional[Literal["previous", "year"]] = None) -> Any:
        """Search traffic by result kind. Google web search clicks and impressions by
        search appearance — rich results, videos, FAQ and review snippets, AMP and the
        other result kinds Search Console reports — two periods compared. Answers 'are
        our rich results earning clicks' and 'did we lose a result type'. Collected from
        the day this was added, and back sixteen months once a connection's history has
        been filled. Free."""
        return self.call("get_search_appearance", _present({"clientId": client_id, "days": days, "compare": compare}))

    def get_search_changes(self, *, client_id: str, days: Optional[int] = None, compare: Optional[Literal["previous", "year"]] = None, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, dimension: Optional[Literal["query", "page"]] = None, brand: Optional[Literal["all", "branded", "non_branded"]] = None, country: Optional[str] = None, device: Optional[Literal["DESKTOP", "MOBILE", "TABLET"]] = None, min_impressions: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """What changed in search. Two periods of Google search compared, by query or by
        page: what is new (shown now, not at all before), what was lost, and the biggest
        gainers and losers by clicks. Answers 'which queries did we start ranking for',
        'what did we lose this week' and 'which pages are growing'. brand narrows to
        branded or non-branded queries (non-branded is what SEO work moves); country and
        device segment it. Periods end on the newest day Google has finished counting.
        searchType reads image, video, news, Discover or Google News instead of web
        (Discover and Google News by page only). Free."""
        return self.call("get_search_changes", _present({"clientId": client_id, "days": days, "compare": compare, "searchType": search_type, "dimension": dimension, "brand": brand, "country": country, "device": device, "minImpressions": min_impressions, "limit": limit}))

    def get_search_console_hourly(self, *, client_id: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, days: Optional[int] = None) -> Any:
        """Search Console clicks and impressions by the hour. Clicks, impressions and
        position from the client's Google Search Console hour by hour over the last 1–10
        days (Google keeps hours for ten days only), read live, for one search type.
        Hours are Pacific time, as Search Console keys them; the newest are partial
        while Google counts and are marked so. Answers 'did traffic dip right after the
        release' and 'is the core update hitting us today'. Free; returns a refusal when
        Search Console is not connected."""
        return self.call("get_search_console_hourly", _present({"clientId": client_id, "searchType": search_type, "days": days}))

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

    def get_search_timeline(self, *, client_id: str, search_type: Optional[Literal["web", "image", "video", "news", "discover", "googleNews"]] = None, from_: Optional[str] = None, to: Optional[str] = None) -> Any:
        """Search traffic with what happened. Daily Google search clicks and impressions
        (and non-branded clicks) beside the client's timeline: deploys, publishes,
        campaigns and notes, and Google's algorithm updates. searchType reads image,
        video, news, Discover or Google News instead of web (non-branded clicks are null
        for the last two, which have no queries). Answers 'what caused this drop' and
        'did the release help'. Free."""
        return self.call("get_search_timeline", _present({"clientId": client_id, "searchType": search_type, "from": from_, "to": to}))

    def get_security_report(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """Security headers and accessibility. Security and accessibility across a crawl:
        how many pages send HSTS (and with a weak max-age), a Content-Security-Policy
        and X-Content-Type-Options: nosniff, pages with mixed content (HTTP images,
        scripts, styles or frames on HTTPS), the security and accessibility checks' page
        counts, and the audit's Lighthouse runs with their accessibility and
        best-practices scores and failed accessibility audits — colour contrast first.
        Answers 'are our security headers set' and 'what accessibility problems does the
        site have'. Free."""
        return self.call("get_security_report", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_seo_changes(self, *, client_id: str, crawl_id: Optional[str] = None, against_crawl_id: Optional[str] = None, fields: Optional[List[Literal["status", "robots", "title", "canonical", "hreflang", "h1", "schema", "description", "og", "h2", "body", "performance"]]] = None, severity: Optional[Literal["critical", "warning", "notice"]] = None, template: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """What changed on the fields search engines read. Compares each page's status,
        robots directives (meta and X-Robots-Tag), canonical, hreflang, title, H1 and
        structured data types between two crawls (default: the latest and the one
        before), counted by field and by URL template, with every change listed.
        Critical: noindex added, canonical changed, title dropped, 200 to 404/5xx,
        hreflang lost, H1 rewritten (under half its words kept) — the changes that cost
        rankings within days, the first five of which each crawl also files as
        regression-* issues. Warning: meta description changed, Open Graph tags removed,
        structured data values changed (schema hash), a Core Web Vital p75 more than 20%
        worse in Chrome's field data, a template's Lighthouse performance down 10 points
        or more. Notice: H2 outline changed, page copy changed (body hash). The
        description, og, h2 and body fields compare only crawls that recorded them.
        fields, severity and template narrow it. Answers 'what did the last release
        break', 'did a template lose its canonicals' and 'why did these pages drop out'.
        Free."""
        return self.call("get_seo_changes", _present({"clientId": client_id, "crawlId": crawl_id, "againstCrawlId": against_crawl_id, "fields": fields, "severity": severity, "template": template, "limit": limit}))

    def get_seo_revenue(self, *, client_id: str, by: Optional[Literal["channel", "landing_page", "query_cluster", "campaign", "source", "ai_referrer", "provider"]] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Revenue by channel, page and query. Imported revenue (orders, revenue net of
        refunds, customers — per currency, never converted) by channel (organic search,
        AI assistants, paid, social, email, referral, direct, unattributed), landing
        page, Search Console query cluster, campaign, source, AI assistant or store,
        with how many orders were matched to their visit. Answers 'what is SEO worth in
        revenue', 'which pages and queries make money', 'what does ChatGPT send us in
        sales'. Free."""
        return self.call("get_seo_revenue", _present({"clientId": client_id, "by": by, "days": days, "limit": limit}))

    def get_seo_scorecard(self, *, client_id: str, crawl_id: Optional[str] = None) -> Any:
        """SEO scorecard with an action plan. One 0–100 score for the site from its latest
        crawl (or crawlId), as seven weighted categories: Technical 22 (crawl, indexing,
        security and URL rules), Content 23 (thin and duplicate content, averaged with
        E-E-A-T over a sample of top pages), On-page 20 (titles, descriptions, headings,
        links, Open Graph), Schema 10 (structured-data rules and the share of pages with
        valid markup), Performance 10 (Chrome UX Report pass 100 / fail 50, averaged
        with the audit's Lighthouse runs), AI readiness 10 (the top pages' answer
        readiness) and Images 5. Each category says how it was measured, or that it was
        not (then the others are rescaled, never scored as zero), with its worst
        findings. Also the business type detected from the homepage and URLs (SaaS,
        local, ecommerce, publisher, agency; stored on the client brief), the five worst
        critical issues, five quick wins (warnings confined to one URL template, so one
        fix clears them) and a four-phase plan: critical issues in week 1, warnings in
        weeks 2–3, content and authority in month 2, then monitoring. Findings accepted
        as intentional (accept_issue) count against nothing and are listed in accepted
        with their reason. A heuristic beside the audit's health score, which is
        unchanged. Answers 'how is the site doing overall' and 'what should we fix
        first'. Free."""
        return self.call("get_seo_scorecard", _present({"clientId": client_id, "crawlId": crawl_id}))

    def get_serp_content_profile(self, *, client_id: str, keyword: str, depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What the ranking pages have in common. Reads the top Google results for a
        keyword and each ranking page, and reports what they share: word count range,
        the outline themes most of them cover, the terms they use and how often, the
        questions they answer, tables, lists, images, video, schema types, reading ease
        and how recently they were updated — plus People Also Ask and related searches,
        and each page's own summary. Results that are not pages to write against —
        videos and Shorts, forum threads, social posts, app store listings — stay in
        pages with their reason in excluded, and are listed in excluded as {url,
        reason}; targetPages counts the rest. Answers 'what does it take to rank for
        this'. The results page is a paid lookup on the client's account unless someone
        bought it in the last day (spend says which); the pages are fetched free. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("get_serp_content_profile", _present({"clientId": client_id, "keyword": keyword, "depth": depth, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_serp_features(self, *, client_id: str, tracker_id: str, device: Optional[Literal["desktop", "mobile"]] = None) -> Any:
        """Get SERP features. Which search features — featured snippet, AI Overview, local
        pack, video, People Also Ask and others — appeared on each tracked keyword's
        latest page, and which the client holds, with totals per feature. Answers 'which
        snippets and overviews do we own'. imagePresence covers image results across
        every keyword the client ranks for: how many ranking pages carry an image pack,
        how many show a client image, and the keywords where it ranks but has no image
        in the pack (best position first) — 'where should we be in image results'.
        Features are null for a capture whose source did not report them, which is not
        the same as a page with none."""
        return self.call("get_serp_features", _present({"clientId": client_id, "trackerId": tracker_id, "device": device}))

    def get_serp_history(self, *, client_id: str, keyword: str, from_: Optional[str] = None, to: Optional[str] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who ranked for a keyword over time. Past Google results pages for any keyword
        (not only tracked ones): for each date, the top results and the features shown.
        Answers 'who used to rank for this', 'when did this competitor take over' and
        'did an update reshuffle this results page'. A paid lookup on the client's
        account unless anyone read the same thing recently (spend says which); quote it
        with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_serp_history", _present({"clientId": client_id, "keyword": keyword, "from": from_, "to": to, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_serp_intent_shifts(self, *, client_id: str, days: Optional[int] = None) -> Any:
        """Keywords whose results page changed character. Tracked keywords whose results
        page changed what it is for between its two latest captures: the mix moving
        (informational, commercial, local, plain — e.g. informational → commercial when
        shopping results arrive) or a watched feature appearing or going (AI Overview,
        video carousel, shopping, map pack, featured snippet, top stories). A page that
        no longer fits the results page's intent loses however good it is. Answers 'did
        Google change what it shows for our keywords' and 'where did AI Overviews
        appear'. Free."""
        return self.call("get_serp_intent_shifts", _present({"clientId": client_id, "days": days}))

    def get_serp_newcomers(self, *, client_id: str, days: Optional[int] = None, baseline_weeks: Optional[int] = None) -> Any:
        """Who is new in the top 20. Domains that entered the top 20 for any of the
        client's tracked keywords in the last days (default 7) and were in none of their
        top 20s in the baselineWeeks before, with the pages they rank with, most
        keywords first. The client's own domain is left out. Answers 'who is new in our
        search results this week' and 'which competitor just started ranking'. Free."""
        return self.call("get_serp_newcomers", _present({"clientId": client_id, "days": days, "baselineWeeks": baseline_weeks}))

    def get_serp_volatility(self, *, client_id: str, tracker_id: Optional[str] = None, days: Optional[int] = None) -> Any:
        """How much the results are moving. How much page one moved between readings for
        each tracked keyword (0 still, ~10 turned over), a daily index for the client's
        keywords beside an industry-wide one from every keyword in the archive, and
        Google's updates in the window. Answers 'is it us or is it Google' when rankings
        move. Free."""
        return self.call("get_serp_volatility", _present({"clientId": client_id, "trackerId": tracker_id, "days": days}))

    def get_share_of_search(self, *, client_id: str, topic: Optional[str] = None, keywords: Optional[List[str]] = None, days: Optional[int] = None) -> Any:
        """The brand's share of each engine. For the client's tracked keywords (narrowed to
        a topic, or to given keywords): one number per engine and the brand's share of
        it — Google, Bing and YouTube (estimated click share from the latest rank
        captures, beside the total search volume), Google's AI Overviews (share of the
        citations they showed), AI Mode and the other AI assistants (share of brand
        mentions in the answers Seolyticize sampled). Read only from stored data, so
        free; an engine with no trackers, captures or sampled answers is listed under
        noData with why. Answers 'where are we visible beyond Google' and 'what share of
        AI answers name us'."""
        return self.call("get_share_of_search", _present({"clientId": client_id, "topic": topic, "keywords": keywords, "days": days}))

    def get_share_of_voice(self, *, client_id: str, tracker_id: str) -> Any:
        """Get share of voice. The client's share of available search clicks across its
        tracked keywords, alongside competitors. Answers 'how much of the market do we
        hold'."""
        return self.call("get_share_of_voice", _present({"clientId": client_id, "trackerId": tracker_id}))

    def get_shopping_keyword_gap(self, *, client_id: str, keywords: Optional[List[str]] = None, sellers: Optional[List[str]] = None, organic_top: Optional[int] = None, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Organic rankings against Google Shopping presence. The client's ranked organic
        keywords (as last synced, top organicTop positions) and any keywords given,
        against whether its products showed in the Google Shopping pages captured by
        get_shopping_serp in the last days, in four groups, each with what to do: both
        (defend), organic_only (ranks but no product listed — list it in Merchant
        Center), shopping_only (a product listed but no organic ranking — build the
        page) and neither. Organic keywords never captured in Shopping are listed apart
        as unchecked, to queue with check_shopping_serp (paid). Matched on the seller
        names given (default the client's name) and the client's domain. Answers 'where
        do we rank but not sell in Shopping' and 'which Shopping keywords need a page'.
        Free."""
        return self.call("get_shopping_keyword_gap", _present({"clientId": client_id, "keywords": keywords, "sellers": sellers, "organicTop": organic_top, "days": days, "limit": limit}))

    def get_shopping_serp(self, *, client_id: str, tasks: List[Dict[str, Any]], sellers: Optional[List[str]] = None, days: Optional[int] = None) -> Any:
        """Google Shopping positions, now and over time. Collects the Shopping pages queued
        by check_shopping_serp, keeps them, and says where the client's products sit —
        matched on the seller names given (default the client's name) and the client's
        domain — with the top listings beside it and the market on each page (price min,
        max, median, P25 and P75 with outliers over 2σ from the median, the top 10
        sellers' share of listings, the share with free shipping and the rating
        distribution), and the client's position history for those keywords from every
        capture kept. A task still queued is listed as pending; ask again shortly.
        Answers 'where do we rank in Google Shopping' and 'who outranks us there'. Free:
        collecting a queued task costs nothing."""
        return self.call("get_shopping_serp", _present({"clientId": client_id, "tasks": tasks, "sellers": sellers, "days": days}))

    def get_site_conventions(self, *, client_id: str, url: Optional[str] = None, samples: Optional[int] = None) -> Any:
        """Site-wide conventions: HSTS preload, slashes, rendering, share image. Four
        site-wide checks from a handful of live requests: whether the base domain
        qualifies for the HSTS preload list (max-age of a year or more,
        includeSubDomains, preload, http:// redirecting to https://; list membership
        itself is not checked); the trailing-slash convention, from up to samples
        crawled paths each asked for with and without the slash (one form redirecting to
        the other is consistent; both answering 200 is two addresses per page unless
        both name one canonical; some paths redirecting each way is mixed); dynamic
        rendering, suspected when Googlebot is served prerendered content and a browser
        an app shell with a fraction of the words (Google calls it a workaround, not a
        recommended solution); and the page's og:image, which should answer 200 and be
        at least 1200×630. url picks the page for the last two (default: the homepage).
        Answers 'are we ready for HSTS preload', 'do we have trailing-slash duplicates'
        and 'is our share image big enough'. Free."""
        return self.call("get_site_conventions", _present({"clientId": client_id, "url": url, "samples": samples}))

    def get_site_status(self, *, client_id: str) -> Any:
        """Site verification and connection status. For a client's sites: whether the
        IndexNow key file has been published and verified, which Search Console
        properties are connected and syncing, and the latest crawl. Answers 'is this
        site set up and verified'."""
        return self.call("get_site_status", _present({"clientId": client_id}))

    def get_snippet_targets(self, *, client_id: str, limit: Optional[int] = None, draft: Optional[bool] = None, read_missing: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Featured snippets within reach. Queries where Google shows a featured snippet or
        People Also Ask and the client ranks 2–10 (Search Console, last 28 days), from
        the stored results pages (readMissing: true buys the ones not stored): who holds
        the snippet, the format to win it — a paragraph of about 45 words, a list or a
        table — and, with draft: true, a draft in that format from one metered Claude
        call for the batch. Answers 'which snippets can we steal' and 'write the answer
        box for this query'. Paid only for drafts and missing results pages; quote it
        with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_snippet_targets", _present({"clientId": client_id, "limit": limit, "draft": draft, "readMissing": read_missing, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_subdomain_traffic(self, *, client_id: str, domain: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """See which subdomains carry a site's search traffic. A site's subdomains ranked
        by estimated organic traffic and ranking keywords, up to 50. Answers 'which
        parts of this site carry its search presence'. get_domain_facts lists subdomain
        names from certificate logs for free but says nothing of their traffic. A paid
        lookup on the client's account: quote it with estimate_cost. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("get_subdomain_traffic", _present({"clientId": client_id, "domain": domain, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_sxo_gap(self, *, client_id: str, url: str, keyword: Optional[str] = None, personas: Optional[bool] = None, wireframe: Optional[bool] = None, deep: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Is this the kind of page Google ranks here. Classifies the client's page and the
        top 10 results for its keyword into claude-seo's eight types (tool, local,
        comparison, product, landing, service, hybrid, else blog, in that order of
        precedence) and says how strongly Google agrees on one type (over 60% strong,
        40–60% mixed, under 40% fragmented) and how bad the page's mismatch is, from an
        explicit page × results table (a blog where products, tools, local pages or
        landing pages rank is critical; a blog against comparisons high; a landing page
        where tools rank high), and which of the expected type's required elements the
        page has. A 0–100 gap score against the ranking pages: page type, depth, UX,
        schema, media and authority 15 each, freshness 10 (null parts drop out). keyword
        defaults to what the title and H1 share, else the page's top Search Console
        query. wireframe: true adds the page's sections now, the target outline and the
        target layout for the page type the results want (landing, blog, product,
        comparison, service, local, tool or hybrid; free); deep: true reads UX from the
        page rendered on a phone (H1 and CTA above the fold, tap targets, font size,
        overlaps, overlays) and authority from its E-E-A-T score beside domain
        authority, and rescores (free, slower); personas: true adds 4–7 searchers from
        People Also Ask, ads and related searches, each a full card (role, goal,
        emotional state, journey stage, key questions, intent) scored on relevance,
        clarity, trust and action (25 each) and rated 80 excellent, 60 good, 40 needs
        work, below a critical mismatch, a persona score weighted by each intent's share
        of the results, and 3–5 user stories ('As a …, I want to …, because …, but I'm
        blocked by …') with their evidence, from one metered Claude call. A heuristic,
        and it says so. Answers 'why doesn't this page rank' and 'what kind of page does
        Google want for this'. The results page is a paid lookup unless bought in the
        last day; quote with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_sxo_gap", _present({"clientId": client_id, "url": url, "keyword": keyword, "personas": personas, "wireframe": wireframe, "deep": deep, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_top_pages(self, *, client_id: str, target: Optional[str] = None, scope: Optional[Literal["auto", "domain", "subdomains", "subfolder", "url"]] = None, limit: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A domain's pages by traffic. A domain's (or subfolder's) pages ranked by
        estimated organic traffic, with how many keywords each ranks for, how many in
        the top 3 and top 10, keywords won and lost, and traffic value. Answers 'which
        pages bring them their traffic' and 'what content works in this niche'. A paid
        lookup on the client's account unless anyone read the same thing recently (spend
        says which); quote it with estimate_cost. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("get_top_pages", _present({"clientId": client_id, "target": target, "scope": scope, "limit": limit, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_top_searches(self, *, market: str, since: str, limit: Optional[int] = None) -> Any:
        """The terms the panel searched most. What a market actually searched for over a
        period, most-searched first, counted by distinct people rather than by events.
        Answers 'what is being looked for right now' for keyword discovery, without a
        vendor's list in between. Terms below the reporting floor never appear."""
        return self.call("get_top_searches", _present({"market": market, "since": since, "limit": limit}))

    def get_topic_map(self, *, client_id: str, seed: Optional[str] = None, days: Optional[int] = None, extra_keywords: Optional[List[str]] = None, method: Optional[Literal["serp_overlap", "search_console"]] = None, limit: Optional[int] = None, min_shared: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Map topics to pages. The client's topics from Search Console (non-branded
        queries, optionally containing a seed) plus any extra keywords, grouped into
        clusters and pillars, each mapped to the pages Google shows for it: no_page
        (write it), one_page, or several_pages (impressions split between pages — merge
        or fix internal links). Answers 'what should we write next', 'which topics have
        no page' and 'where are our pages competing'. method serp_overlap clusters by
        results-page overlap (one paid lookup per keyword unless bought in the last
        day); search_console clusters by the page each query lands on, free. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_topic_map", _present({"clientId": client_id, "seed": seed, "days": days, "extraKeywords": extra_keywords, "method": method, "limit": limit, "minShared": min_shared, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_topical_authority(self, *, client_id: str, days: Optional[int] = None, seed: Optional[str] = None, extra_keywords: Optional[List[str]] = None, limit: Optional[int] = None) -> Any:
        """How strong the site is on each topic. A 0–100 topical authority score per topic
        (the topic map's pillars, from Search Console): coverage (the share of the
        topic's query clusters with a page ranking in the top 20) × rankings
        (impression-weighted) × internal links (links into each covering page, from the
        latest crawl) — each part given — and the next three pages that would raise it
        most: write (a cluster nothing covers), improve (a page beyond the first page)
        or link (a weakly linked page). extraKeywords adds topics the site does not rank
        for yet. Answers 'where are we an authority' and 'what should we write next to
        own this topic'. Free."""
        return self.call("get_topical_authority", _present({"clientId": client_id, "days": days, "seed": seed, "extraKeywords": extra_keywords, "limit": limit}))

    def get_toxic_link_risk(self, *, client_id: str, money_terms: Optional[List[str]] = None, spam_scores: Optional[Dict[str, Any]] = None, fetch_spam_scores: Optional[bool] = None, min_verdict: Optional[Literal["review", "toxic"]] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Which linking sites are a risk, and why. Judges each site linking to the client
        from the evidence a person can check: the vendor's spam score (fetchSpamScores:
        true buys it for every linking site inside this call — one paid DataForSEO
        request of up to 1,000 sites, the price of get_backlink_spam_scores, with sites
        scored in the last 30 days reused free; or pass spamScores you already have),
        sitewide links (the link on most of the pages we hold of the site: a footer or
        blogroll), link-seller neighbourhoods (a site linking out to hundreds of domains
        from few pages), commercial exact-match anchors (pass moneyTerms; brand terms
        are excluded), the vendor links' own authority and outbound signals, and
        claude-seo's thirty toxic patterns where the data allows (a page with 10,000+ or
        50+ outbound links, a domain registered under 30 days ago with 100+ outbound
        links or re-registered after it lapsed — from RDAP for the sites linking out
        most — pharma or casino injections, sitewide links and exact-match anchors from
        unrelated sites, foreign-language and parked sites, article directories, forum
        profiles, press release wires, coupon sites, comment links, unrelated niches
        when moneyTerms say what the client does), each pattern reported flagged, clear
        or unmeasured with why. disavow says whether a file is worth making (toxic over
        10% of the sites: yes; under 2%: no). A verdict (healthy, review, toxic) and
        every reason with its detail; whether the last saved disavow file already names
        the site, and the toxic sites that appeared since it. Answers 'which of our
        links are toxic and why' and 'what should go in the disavow file now'. 'review'
        means look, not disavow. Free without fetchSpamScores; with it, quote it with
        estimate_cost or dryRun first. Can spend: pass max_cost_micros to cap it."""
        return self.call("get_toxic_link_risk", _present({"clientId": client_id, "moneyTerms": money_terms, "spamScores": spam_scores, "fetchSpamScores": fetch_spam_scores, "minVerdict": min_verdict, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_tracker_ai_mode(self, *, client_id: str, tracker_id: str, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """AI Mode beside each ranking. Reads Google AI Mode for a tracker's keywords (up
        to limit) and puts beside each latest position whether AI Mode cites the client
        and which domains it cites — the gap between ranking and being the answer. One
        paid AI Mode read per keyword: quote it with estimate_cost first. Answers 'we
        rank for these, but does AI Mode cite us'. Can spend: pass max_cost_micros to
        cap it."""
        return self.call("get_tracker_ai_mode", _present({"clientId": client_id, "trackerId": tracker_id, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_translation_gap(self, *, client_id: str, crawl_id: Optional[str] = None, examples: Optional[int] = None) -> Any:
        """Pages missing in a language. Which pages exist in one language and not another:
        each indexable page's language (its hreflang, its /es/-style path prefix or its
        html lang), versions matched by hreflang or by the same path without the prefix,
        and for each language its coverage of the main language with the pages it lacks.
        Answers 'which pages have no Spanish version' and 'how complete is our /es
        site'. Free."""
        return self.call("get_translation_gap", _present({"clientId": client_id, "crawlId": crawl_id, "examples": examples}))

    def get_trust_signals(self, *, client_id: str) -> Any:
        """Who stands behind the site. Checks the signals of who is behind a site that
        Google's quality raters and AI assistants weigh (E-E-A-T): an about page, a
        contact page with a way to reach a person, a privacy policy and terms,
        Organization structured data on the homepage, named authors and publish dates on
        articles, and HTTPS. Each pass, fail or unknown, with what was found. Answers
        'does our site show who we are' and 'what trust signals are missing'. Free."""
        return self.call("get_trust_signals", _present({"clientId": client_id}))

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

    def get_vendor_reconciliation(self) -> Any:
        """Reconcile vendor spend against the ledger. Sets the agency's DataForSEO account
        (deposited, balance, spent; today's spend per API) beside what Seolyticize's
        cost ledger recorded on the same account, with the difference, the ledger by
        operation, and what can explain a gap: spend before the ledger began, the same
        login used outside Seolyticize, other agencies sharing it. Answers 'why did our
        DataForSEO balance fall more than get_costs shows'. agreesWithinCents is true
        when the two agree to a cent. Reads the account from DataForSEO's free user_data
        endpoint. On the platform's shared key, only a platform admin may reconcile.
        Amounts are US dollars. Free."""
        return self.call("get_vendor_reconciliation", {})

    def get_vitals_history(self, *, client_id: str, url: Optional[str] = None, form_factor: Optional[Literal["phone", "desktop", "all"]] = None) -> Any:
        """Core Web Vitals over 25 weeks. Core Web Vitals as Chrome measured them, week by
        week for the last 25 weeks, from the Chrome UX Report History API: p75 LCP, INP,
        CLS, TTFB and FCP (good at 1.8 s or less, poor over 3 s) for the client's
        origin, or one URL (url) when it has enough traffic, by form factor (phone,
        desktop or all). Regressions name a metric that got worse by more than 10% over
        the last four weeks or crossed into a worse rating; trends compare the first
        four weeks with the last four (within ±5% is stable). lcpBreakdown splits the
        newest image LCP into Chrome's four subparts (time to first byte, resource load
        delay, load duration, render delay) and names any at 40% of p75 LCP or more,
        with what to fix. Also the audits' Lighthouse runs per template, for the lab
        side. Without a Chrome UX Report key it says so and shows what is stored;
        nothing is estimated. Answers 'did our Core Web Vitals get worse', 'when did LCP
        regress' and 'are we passing on mobile'. Free."""
        return self.call("get_vitals_history", _present({"clientId": client_id, "url": url, "formFactor": form_factor}))

    def get_volume_calibration(self, *, client_id: str) -> Any:
        """How far vendor volumes are off for this site. The correction factor between the
        vendor's search volumes and what Search Console counted, per market: for queries
        where the site held positions 1–3 (where impressions are close to searches), the
        median of impressions over volume, with how many terms it rests on and their
        spread. Keyword tools add calibratedVolume next to volume where a factor exists.
        Answers 'can we trust these search volumes' and 'why does Search Console show
        more searches than the keyword tool'. Free."""
        return self.call("get_volume_calibration", _present({"clientId": client_id}))

    def get_web_analytics_breakdown(self, *, client_id: str, breakdown: Literal["pages", "entry_pages", "exit_pages", "sources", "referrers", "campaigns", "countries", "devices", "browsers", "os", "events", "channels", "ai_sources", "ai_landing_pages"], days: Optional[float] = None, limit: Optional[int] = None) -> Any:
        """Traffic by page, source, campaign, country or device (first-party). Lists the
        top rows of one breakdown from Seolyticize's own web analytics: pages
        (pageviews), entry_pages and exit_pages (visits), sources and referrers (visits;
        key null means direct), campaigns (visits, with detail "source / medium"),
        countries (ISO codes; null means unknown), devices, browsers, os, custom events
        (event count), channels (visits by channel: AI, Organic Search, Paid Search,
        Social, Email, Referral, Campaign, Direct), ai_sources (visits from each AI
        assistant: ChatGPT, Perplexity, Gemini, Copilot, Claude, Google AI Mode and
        others) or ai_landing_pages (the pages AI assistants send visits to, detail
        naming the assistant). Each row has key, visitors and count; counts says what
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

    def get_yandex_diagnostics(self, *, client_id: str) -> Any:
        """What Yandex says is wrong with the site. Yandex Webmaster's site diagnostics:
        each check (robots.txt blocking the site, DNS or SSL errors, a slow server,
        missing or broken sitemaps, duplicate pages, missing titles, not mobile
        friendly...) with its severity and whether the problem is present now, worst
        first. Answers 'does Yandex see anything broken'. Free."""
        return self.call("get_yandex_diagnostics", _present({"clientId": client_id}))

    def get_yandex_external_links(self, *, client_id: str, offset: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Links Yandex knows point at the site. Yandex's count of external links to the
        client's host over time, and a page of the links themselves (source page, the
        page of ours it points to, when Yandex found it). Answers 'is our link count
        growing in Yandex' and 'who links to us, per Yandex'. Free."""
        return self.call("get_yandex_external_links", _present({"clientId": client_id, "offset": offset, "limit": limit}))

    def get_yandex_important_pages(self, *, client_id: str) -> Any:
        """The pages Yandex is watching for the site. Yandex Webmaster's important-pages
        monitoring: each page the site owner chose to watch, with its last crawl status
        and HTTP code, whether it is searchable, its title and description in Yandex,
        why it is excluded if it is, and what changed since the previous check. Answers
        'are our key pages still in Yandex'. Pages are chosen in Yandex Webmaster
        itself; the API only reads them. Free."""
        return self.call("get_yandex_important_pages", _present({"clientId": client_id}))

    def get_yandex_indexing(self, *, client_id: str, from_: str, to: str, offset: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """Which pages Yandex has in search. Yandex Webmaster's indexing views for the
        client's verified host: pages in search by day and a sample of them, pages that
        appeared in or were removed from search by day and a sample with Yandex's reason
        for each removal (duplicate, not canonical, noindex, HTTP error, low quality...)
        counted by reason, and a sample of what the robot fetched with the status it
        got. Answers 'which pages has Yandex dropped, and why'. Samples are paged (limit
        up to 100). Free."""
        return self.call("get_yandex_indexing", _present({"clientId": client_id, "from": from_, "to": to, "offset": offset, "limit": limit}))

    def get_yandex_performance(self, *, client_id: str, from_: str, to: str) -> Any:
        """What Yandex Webmaster reports. The client's site as Yandex Webmaster reports it:
        site quality index, searchable and excluded pages, problems by severity, popular
        search queries with impressions, clicks and position, indexing history by HTTP
        status, sitemaps, and the recrawl queue with its quota. Answers 'how is this
        site doing in Yandex'. configured is false when this deployment has no Yandex
        app, and connected is false until the client's site owner has granted access."""
        return self.call("get_yandex_performance", _present({"clientId": client_id, "from": from_, "to": to}))

    def get_yandex_query_history(self, *, client_id: str, from_: str, to: str, device: Optional[Literal["ALL", "DESKTOP", "MOBILE_AND_TABLET", "MOBILE", "TABLET"]] = None, query_id: Optional[str] = None) -> Any:
        """Yandex search traffic by day. Yandex Webmaster's search query history: shows,
        clicks and average show and click position by day for the whole site, or for one
        query (queryId, from get_yandex_performance's queries), optionally for one
        device. Answers 'how has our Yandex traffic moved' and 'how is this query
        trending in Yandex'. Free."""
        return self.call("get_yandex_query_history", _present({"clientId": client_id, "from": from_, "to": to, "device": device, "queryId": query_id}))

    def get_youtube_channel_rankings(self, *, client_id: str, channel: str, keywords: List[str], depth: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Which of a channel's videos rank, for which phrases. For up to 20 phrases, reads
        YouTube's results and lists every video from the channel (matched by channel id,
        or by name) with its position and views, and the phrases where the channel does
        not appear. Works for the client's channel or a competitor's. For tracking over
        time, a rank tracker on the youtube engine does the same daily. Answers 'where
        do our videos rank' and 'which of their videos rank for our topics'. One results
        page per phrase: A paid lookup on the client's account unless anyone read the
        same thing today (spend says which); quote it with estimate_cost. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("get_youtube_channel_rankings", _present({"clientId": client_id, "channel": channel, "keywords": keywords, "depth": depth, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def get_zero_click_estimates(self, *, client_id: str, days: Optional[int] = None, limit: Optional[int] = None) -> Any:
        """How many searches end without a click. For each Search Console query that a
        tracked keyword's latest capture describes, the estimated share of searches that
        end with no organic click, from the features on its results page (AI Overview,
        featured snippet, map pack, shopping, knowledge panel, video…) — measured on
        this site's own click-through curve where it can be, a published share otherwise
        (source says which) — and how many of the query's searches that is. Answers 'how
        much demand is the AI Overview eating' and 'which keywords are worth less than
        their volume says'. Free."""
        return self.call("get_zero_click_estimates", _present({"clientId": client_id, "days": days, "limit": limit}))

    def import_revenue_now(self, *, client_id: str, provider: Optional[Literal["stripe", "shopify", "paddle"]] = None) -> Any:
        """Import orders now. Imports what changed in the client's connected stores since
        the last import (the nightly import does this on its own), attributing each
        order to the visit it came from. Answers 'pull in today's orders'. Free."""
        return self.call("import_revenue_now", _present({"clientId": client_id, "provider": provider}))

    def inspect_bing_url(self, *, client_id: str, url: str) -> Any:
        """Ask Bing what it holds for one page. Bing's index details for one address on the
        client's site (GetUrlInfo): when Bing discovered and last crawled it, the HTTP
        status and size it got, links pointing at it and, for a directory, how many
        pages sit under it — plus its Bing clicks and impressions. Answers 'is this page
        in Bing, and when did Bing last see it'. Free; no daily allowance."""
        return self.call("inspect_bing_url", _present({"clientId": client_id, "url": url}))

    def inspect_url(self, *, client_id: str, url: str) -> Any:
        """Ask Google what it holds for one page. Runs Google's URL Inspection on one
        address of the client's own site: whether it is indexed, Google's coverage
        state, when it was last crawled, Google's chosen canonical against the site's
        own, mobile usability (deprecated by Google and often absent) and rich results
        detected. Answers 'is this page in Google, and if not why'. Spends one of the
        property's 2,000 daily inspections; refuses addresses that are not on a site the
        agency manages for this client, and says so when the day's allowance is used."""
        return self.call("inspect_url", _present({"clientId": client_id, "url": url}))

    def invite_team_member(self, *, email: str, role: Literal["admin", "manager", "analyst", "client_viewer"], client_ids: Optional[List[str]] = None) -> Any:
        """Invite someone to the team by email. Emails an invitation to join the agency
        with a role — admin, manager, analyst or client_viewer — optionally limited to
        some clients. Unlike add_team_member the person need not have an account yet:
        they sign up or sign in, as the invited address, and the link makes them a
        member. The link lasts 7 days and works once. Answers 'invite sam@agency.com as
        an analyst on Acme'. Returns the invite, whether the email was sent, and the
        link itself for passing on by hand. Refused for an existing member, an address
        with a live invite (use resend_team_invite), or a client outside the caller's
        reach."""
        return self.call("invite_team_member", _present({"email": email, "role": role, "clientIds": client_ids}))

    def issue_indexnow_key(self, *, client_id: str) -> Any:
        """Issue an IndexNow key. Issues the client's IndexNow key and returns the file to
        put on the site: fileName at the site's root, containing exactly the key.
        Answers 'set up IndexNow'. Re-issuing replaces the key and invalidates the file
        already on the site, so only do it when asked to or when the key must be
        retired. Hand the file to whoever can publish to the site (sites running the
        Seolyticize WordPress plugin serve it themselves), then call
        verify_indexnow_key."""
        return self.call("issue_indexnow_key", _present({"clientId": client_id}))

    def issue_server_collect_key(self, *, client_id: str) -> Any:
        """Key for server-side collection. Issues the secret key a server-side collector
        (@seolyticize/next/server, the Python and PHP collectors, or a POST to
        /api/collect with Authorization: Bearer) reports with, so it may send each
        visitor's own address and user agent (body fields ip and ua; howToUse lists the
        rest) — which is what lets it count people, and the AI assistants (ChatGPT-User,
        Claude-User, Perplexity-User) that never run the browser tag. Shown once;
        issuing another revokes the last. Answers 'track visits from our server' and
        'count AI agents reading our pages'. Free."""
        return self.call("issue_server_collect_key", _present({"clientId": client_id}))

    def issue_site_verification(self, *, client_id: str, method: Optional[Literal["file", "meta", "dns"]] = None, site_url: Optional[str] = None) -> Any:
        """Issue a Google site verification. Answers 'prove we own the site to Google
        without anyone opening Search Console'. Asks Google for a verification token for
        the agency's own Google account and returns what to deploy: a file at the site
        root (file), a <head> tag (meta) or a TXT record (dns). Then call
        verify_site_ownership. onboard_site does this for you. Free."""
        return self.call("issue_site_verification", _present({"clientId": client_id, "method": method, "siteUrl": site_url}))

    def keyword_explorer(self, *, client_id: str, seed: str, mode: Optional[Literal["ideas", "suggestions", "related", "questions"]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, filters: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, page: Optional[int] = None, page_size: Optional[int] = None, format_: Optional[Literal["rows", "csv"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Explore keyword ideas with filters. Expands a seed term into keyword ideas,
        suggestions, related terms or questions, then filters, sorts and pages them:
        include and exclude words, volume, difficulty, cost per click and word-count
        ranges, questions only, search intent, and result-page features. Answers 'which
        terms around this topic are worth going after'. The expansion is bought once per
        seed, mode and market; every later filter on the same seed is free. Rows a
        filter cannot judge because the number is unknown are left out and counted in
        unknownExcluded rather than treated as zero. Set format to csv for every
        matching row as a CSV file. Can spend: pass max_cost_micros to cap it."""
        return self.call("keyword_explorer", _present({"clientId": client_id, "seed": seed, "mode": mode, "locationCode": location_code, "languageCode": language_code, "filters": filters, "sort": sort, "page": page, "pageSize": page_size, "format": format_, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def keyword_traffic_potential(self, *, client_id: str, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, refresh: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What ranking first for a keyword is worth. Traffic potential and parent topic
        for a keyword: the estimated monthly organic traffic of the page ranking first,
        summed across every keyword that page ranks for, and that page's highest-volume
        keyword. Answers 'how much traffic is this keyword really worth' and 'what topic
        should the page be about' — a keyword's own volume undersells it. Estimated
        through the measured click curve and labelled with its source. Null when the
        leader's rankings are unknown, never zero. May buy the results page and the
        leader's ranked keywords when the archive holds neither. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("keyword_traffic_potential", _present({"clientId": client_id, "term": term, "locationCode": location_code, "languageCode": language_code, "refresh": refresh, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def list_accepted_issues(self, *, client_id: str, include_lapsed: Optional[bool] = None) -> Any:
        """List the issues accepted as intentional. The client's accepted audit findings:
        rule, template or addresses, the reason, until and who accepted it.
        includeLapsed adds the ones whose until has passed, which count again. Answers
        'what have we decided to ignore, and why'. Free."""
        return self.call("list_accepted_issues", _present({"clientId": client_id, "includeLapsed": include_lapsed}))

    def list_alert_rules(self, *, client_id: str) -> Any:
        """List alert rules. What a client's alerts watch for, at what threshold, and
        whether each is paused and can be delivered (hasDeliveryTarget false: it fires
        into nothing; undeliverable lists those rules with the fix). Lists the rules;
        list_recent_alerts lists what they fired. add_default_alerts adds the starting
        four."""
        return self.call("list_alert_rules", _present({"clientId": client_id}))

    def list_annotations(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, include_google: Optional[bool] = None) -> Any:
        """List the client's timeline. The client's timeline notes between two days, oldest
        first, with Google's algorithm updates when includeGoogle is true. Answers 'what
        changed around then'. Free."""
        return self.call("list_annotations", _present({"clientId": client_id, "from": from_, "to": to, "includeGoogle": include_google}))

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

    def list_client_facts(self, *, client_id: str) -> Any:
        """List the client's canonical facts. The client's registered facts by category:
        key, value, terms and source. Answers 'what do we hold as true about this
        client'. Free."""
        return self.call("list_client_facts", _present({"clientId": client_id}))

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

    def list_content_plan(self, *, client_id: str, from_: Optional[str] = None, to: Optional[str] = None, status: Optional[List[Literal["planned", "briefed", "drafting", "published", "dropped"]]] = None, plan_id: Optional[str] = None) -> Any:
        """List the editorial calendar. The client's planned content, month by month:
        keyword, kind (new or refresh), target URL, status, brief arguments, internal
        links and estimated value. Filter by month range, status or one plan. Answers
        'what is planned for next month'. Free."""
        return self.call("list_content_plan", _present({"clientId": client_id, "from": from_, "to": to, "status": status, "planId": plan_id}))

    def list_conversion_goals(self, *, client_id: str, days: Optional[int] = None) -> Any:
        """The events a site sends. The custom events the client's site sends to the
        cookieless analytics, most-sent first, with how many carry a value — the goals
        get_conversions can count. Answers 'what are we tracking'. Says how to send one
        when there are none. Free."""
        return self.call("list_conversion_goals", _present({"clientId": client_id, "days": days}))

    def list_crawl_issues(self, *, client_id: str, crawl_id: Optional[str] = None, indexable_only: Optional[bool] = None) -> Any:
        """List site audit issues. Technical issues one crawl found, by rule: its readable
        label, severity, category, how many pages it affects, and howToFix — concrete
        steps to fix it and check the fix. Lists what to fix. Use crawlId 'latest' for
        the newest completed crawl. indexableOnly (default true) leaves out findings on
        pages search engines will not index as themselves — noindexed, not answering
        200, or canonicalised elsewhere — except the findings that explain why; pass
        false to see everything."""
        return self.call("list_crawl_issues", _present({"clientId": client_id, "crawlId": crawl_id, "indexableOnly": indexable_only}))

    def list_crawls(self, *, client_id: str, limit: Optional[int] = None) -> Any:
        """List crawls. A client's recent crawls of every status, newest first. Lists what
        the crawler has been doing, including crawls that failed."""
        return self.call("list_crawls", _present({"clientId": client_id, "limit": limit}))

    def list_data_syncs(self, *, client_id: str) -> Any:
        """List data syncs. Lists every scheduled data sync for the client: what it
        queries, where it writes, how often, when it last ran, how many rows and any
        error. Free."""
        return self.call("list_data_syncs", _present({"clientId": client_id}))

    def list_digest_schedules(self, *, client_id: str) -> Any:
        """List digest schedules. Lists where and when the client's weekly digest is
        posted, and when it last went. Free."""
        return self.call("list_digest_schedules", _present({"clientId": client_id}))

    def list_funnels(self, *, client_id: str) -> Any:
        """List funnels. Lists the funnels defined for a client, with their steps. Free."""
        return self.call("list_funnels", _present({"clientId": client_id}))

    def list_goals(self, *, client_id: str) -> Any:
        """List conversion goals. The goals defined for a client's cookieless analytics,
        with what each matches and its value. Lists what get_goal_report counts;
        list_conversion_goals shows the custom events being sent. Free."""
        return self.call("list_goals", _present({"clientId": client_id}))

    def list_integrations(self, *, client_id: str) -> Any:
        """A client's connected tools. Lists every outside service connected for the client
        — stores, sheets, Airtable, BigQuery, chats, trackers — with how it was
        connected, the key's last characters, when it last worked and its last error.
        Never the secret. Free."""
        return self.call("list_integrations", _present({"clientId": client_id}))

    def list_invite_codes(self) -> Any:
        """List invite codes. Lists the agency's invite codes — label, uses left, expiry,
        whether revoked — never the codes themselves. Answers 'which invite codes are
        out there'. Free."""
        return self.call("list_invite_codes", {})

    def list_issue_pages(self, *, client_id: str, rule_id: str, crawl_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, indexable_only: Optional[bool] = None) -> Any:
        """List the pages an issue is on. Lists the pages where one crawl issue was found,
        with the message for each page, so they can be fixed. Answers 'which pages have
        missing titles' or 'where are the broken links'. ruleId comes from
        get_audit_summary or list_crawl_issues; crawlId defaults to the latest completed
        crawl. Paged: limit (up to 500) and offset; total is the whole count.
        indexableOnly (default true) leaves out findings on pages search engines will
        not index as themselves — noindexed, not answering 200, or canonicalised
        elsewhere — except the findings that explain why; pass false to see everything.
        Each page carries its path owner (owner, from set_path_owners) and, when
        accept_issue covers it, accepted with the reason. Free."""
        return self.call("list_issue_pages", _present({"clientId": client_id, "ruleId": rule_id, "crawlId": crawl_id, "limit": limit, "offset": offset, "indexableOnly": indexable_only}))

    def list_keyword_lists(self, *, client_id: Optional[str] = None) -> Any:
        """List keyword lists. The keyword lists the caller can see, with how many keywords
        each holds — one client's, or every list the caller may reach when no client is
        named. Answers 'where did we save those keywords'. The agency's own lists, which
        belong to no client, are only visible to people who can see every client."""
        return self.call("list_keyword_lists", _present({"clientId": client_id}))

    def list_keyword_owners(self, *, client_id: str, url: Optional[str] = None) -> Any:
        """Which page owns which keyword. The client's keyword-to-page registry: each
        keyword (with its cluster) and the page that owns it, optionally for one page.
        Answers 'which keywords is /blog/x meant to rank for' and 'who owns this query'.
        Free."""
        return self.call("list_keyword_owners", _present({"clientId": client_id, "url": url}))

    def list_lead_widgets(self) -> Any:
        """List lead-gen widgets. The agency's audit forms, each with its embed code,
        allowed sites, who is notified and whether it is switched on. Answers 'which
        audit forms do we have on our sites'. Free."""
        return self.call("list_lead_widgets", {})

    def list_leads(self, *, widget_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """List leads from audit widgets. People who asked for an audit through the
        agency's widgets, newest first: email, the page they checked, where the form
        was, the audit they were shown (counts, page title and findings), and whether
        the agency was emailed (notifyError says why not). Answers 'who filled in our
        audit form'. Free."""
        return self.call("list_leads", _present({"widgetId": widget_id, "limit": limit}))

    def list_link_prospects(self, *, client_id: str) -> Any:
        """List a client's link prospects. The client's outreach list: sites worth asking
        for a link, each with its stage (identified, contacted, replied, won, rejected),
        why it was added, when it last moved, the contact to write to and, for won
        links, whether the last link check found the link live on its page — most
        recently moved first. Answers 'where is our link outreach' and 'are the links we
        won still up'. Free."""
        return self.call("list_link_prospects", _present({"clientId": client_id}))

    def list_local_locations(self, *, client_id: str) -> Any:
        """List a client's business locations. The client's business locations for local
        SEO: id, name, latitude and longitude. Answers 'which locations do we track in
        the map pack'. Pass an id to get_local_visibility, run_local_grid_scan or
        sync_local_reviews. Free."""
        return self.call("list_local_locations", _present({"clientId": client_id}))

    def list_log_sources(self, *, client_id: str) -> Any:
        """Connected log feeds. The client's connected log feeds: kind, when each last
        delivered, how many crawler requests it has stored and its last error (an S3
        pull that was refused, say). Ingest URLs and keys are never shown again. Answers
        'are our logs still arriving'. Free."""
        return self.call("list_log_sources", _present({"clientId": client_id}))

    def list_markets(self, *, query: Optional[str] = None) -> Any:
        """Find a market's location code. Lists the countries and regions this product
        measures, with the location code other tools take (locationCode), the ISO code
        and Google's own country code. Search by name, ISO code (gb), Google code (uk)
        or location code (2826); an exact code wins over a name match. Answers 'what is
        the location code for Germany'. Only markets the product can measure honestly
        are listed. Free."""
        return self.call("list_markets", _present({"query": query}))

    def list_outreach_sequences(self, *, client_id: str) -> Any:
        """The client's outreach sequences. The sequences saved for the client, newest
        first, with their steps. Answers 'which sequences do we have'. Free."""
        return self.call("list_outreach_sequences", _present({"clientId": client_id}))

    def list_path_owners(self, *, client_id: str) -> Any:
        """List who owns which part of the site. The client's path owners from
        set_path_owners: prefix, owner and contact, shortest prefix first. Answers 'who
        fixes issues on /docs'. Free."""
        return self.call("list_path_owners", _present({"clientId": client_id}))

    def list_portal_links(self, *, client_id: str) -> Any:
        """List client portal links. The live white-label portal links for a client: label,
        when each was made, and when it was last opened. Lists who can currently see the
        client's results without an account. The addresses themselves are not shown —
        they exist only at the moment a link is made."""
        return self.call("list_portal_links", _present({"clientId": client_id}))

    def list_portfolios(self) -> Any:
        """List portfolios. The agency's portfolios — named groups of clients or single
        sites — with their members. A viewer limited to some clients sees only their
        members, with a count of the rest. Answers 'which client groups do we have'.
        Free."""
        return self.call("list_portfolios", {})

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

    def list_report_links(self, *, client_id: Optional[str] = None) -> Any:
        """List live report links. The share links made with create_report_link that still
        open, newest first, for one client or (without clientId) every client the caller
        can see: each with linkId, the report, its period, when it was made and by whom,
        when it expires, and when it was last opened (lastViewedAt, null if never) with
        a view count. Answers 'which report links are out there' and 'has the client
        opened the report'. The address itself is not returned: it is a secret shown
        once and never stored, so make a new link to send it again. Free."""
        return self.call("list_report_links", _present({"clientId": client_id}))

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

    def list_task_links(self, *, client_id: str) -> Any:
        """Tasks mirrored in trackers. Lists which of the client's tasks are mirrored as
        issues, where (PROJ-12, ENG-34, #56, with links), and the tracker's state as
        last read. Free."""
        return self.call("list_task_links", _present({"clientId": client_id}))

    def list_tasks(self, *, client_id: str, statuses: Optional[List[Literal["todo", "in_progress", "done", "wont_do"]]] = None, assignee_user_id: Optional[str] = None, unassigned_only: Optional[bool] = None, limit: Optional[int] = None) -> Any:
        """List a client's tasks. A client's tasks, open ones first and soonest due first:
        title, status, assignee, due date, whether overdue, and the issue, page or
        keyword each is about. Answers 'what is left to do for Acme' and 'what is Sam
        working on'. Filter by status and assignee. Free."""
        return self.call("list_tasks", _present({"clientId": client_id, "statuses": statuses, "assigneeUserId": assignee_user_id, "unassignedOnly": unassigned_only, "limit": limit}))

    def list_team_invites(self) -> Any:
        """List pending invites. Invites not yet accepted or withdrawn, newest first, with
        role, client scope, when each expires and how often it was sent. Expired ones
        are listed so they can be resent. Answers 'who have we invited who has not
        joined'."""
        return self.call("list_team_invites", {})

    def list_team_members(self) -> Any:
        """List the team. Everyone with access to the agency: email, name, role, and the
        clients each is limited to (empty means agency-wide). Also lists the clients a
        new member could be limited to. Answers 'who can see this account'."""
        return self.call("list_team_members", {})

    def list_tracked_keywords(self, *, client_id: str, tracker_id: str) -> Any:
        """List tracked keywords. The terms a tracker measures and the competitor domains
        it compares against. Lists what is being paid for on every run."""
        return self.call("list_tracked_keywords", _present({"clientId": client_id, "trackerId": tracker_id}))

    def list_webhook_deliveries(self, *, webhook_id: str, limit: Optional[int] = None) -> Any:
        """A webhook's deliveries. A webhook's recent deliveries, newest first: event,
        status, attempts, the receiver's last HTTP status and error. Answers 'why isn't
        my webhook receiving anything'. Free."""
        return self.call("list_webhook_deliveries", _present({"webhookId": webhook_id, "limit": limit}))

    def list_webhooks(self) -> Any:
        """List webhooks. The agency's webhooks: URL, events, client, and whether one was
        switched off after failing for too long. Answers 'what webhooks do we have'.
        Free."""
        return self.call("list_webhooks", {})

    def list_written_reports(self, *, client_id: str) -> Any:
        """List written reports. Lists the written reports saved for a client, newest
        change first: id, title, a plain-text summary, who wrote and last changed it,
        and whether it is shared. Answers 'what reports have we written for this
        client'. Call it before save_written_report to find a report to replace rather
        than writing a duplicate. Free."""
        return self.call("list_written_reports", _present({"clientId": client_id}))

    def mine_app_reviews(self, *, client_id: str, store: Literal["app_store", "google_play"], app_id: str, location_code: Optional[int] = None, language_code: Optional[str] = None, limit: Optional[int] = None, task_id: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What an app's reviews keep saying. Reads an app's recent reviews and mines them:
        the rating split, themes (crashes and bugs, performance, sign-in, ads, pricing
        and subscriptions, support, design, features) with how often each is raised and
        how negative, the phrases most repeated in 1–2 star reviews and in 4–5 star
        ones, and the feature requests. Works on a competitor's app as well as the
        client's. App Store reviews come free from Apple's public reviews feed (most
        recent 500); Google Play reviews through DataForSEO's App Data, queued: pending
        with a taskId to pass again when not back within half a minute. Answers 'what do
        users complain about', 'what do they love' and 'what are they asking for'. App
        Store: free. Google Play: A paid lookup on the client's account (spend says how
        much); quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("mine_app_reviews", _present({"clientId": client_id, "store": store, "appId": app_id, "locationCode": location_code, "languageCode": language_code, "limit": limit, "taskId": task_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def notify_google_indexing(self, *, client_id: str, urls: List[str], type_: Optional[Literal["URL_UPDATED", "URL_DELETED"]] = None, dry_run: Optional[bool] = None) -> Any:
        """Tell Google a job posting or livestream changed. Sends Google's Indexing API a
        notification for each address: URL_UPDATED for a new or changed page,
        URL_DELETED for one taken down. Google accepts it only for pages with JobPosting
        markup or a BroadcastEvent inside a VideoObject, so each page is checked first —
        read live for an update, from the latest crawl for a removal — and any other
        page is refused with the reason (use submit_indexnow or a sitemap for those). At
        most 200 a day per agency. Needs Search Console connected as the agency's Google
        account (verify_site) with that account an Owner of the property; a Google
        sign-in connection cannot send these. dryRun: true checks every page the same
        way but sends nothing and spends none of the daily allowance, returning
        wouldSubmit and refused. Answers 'get this job posting indexed now' and 'tell
        Google the vacancy is filled'."""
        return self.call("notify_google_indexing", _present({"clientId": client_id, "urls": urls, "type": type_, "dryRun": dry_run}))

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

    def page_headers(self, *, url: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """What the server actually returned. Status code, redirect chain, content type and
        the headers that decide indexing for one address. Answers 'why is this page not
        in the index' when the markup looks fine — an X-Robots-Tag noindex is invisible
        to anything reading the page. Can spend: pass max_cost_micros to cap it."""
        return self.call("page_headers", _present({"url": url, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def page_lab(self, *, url: str, strategy: Optional[Literal["mobile", "desktop"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """How a page scores in one synthetic run. Lighthouse performance, SEO,
        accessibility and best-practices scores for one address, from PageSpeed
        Insights. Answers 'what is slow or wrong on this page' with a reproducible lab
        run, including for pages too quiet for field data. diagnostics says where the
        time went — the LCP element and its subparts (TTFB, resource load delay,
        resource load duration, element render delay), DOM size, long tasks, main-thread
        work, script execution, render-blocking requests, unused JavaScript and CSS,
        third parties — and fixes ranks the findings by estimated saving. This is not
        what real visitors experienced — use page_vitals for that, and say which is
        which when reporting both. There is no interaction metric here: a synthetic run
        interacts with nothing. Can spend: pass max_cost_micros to cap it."""
        return self.call("page_lab", _present({"url": url, "strategy": strategy, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

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

    def plan_content(self, *, client_id: str, months: Optional[int] = None, cadence: Optional[Literal["weekly", "fortnightly", "monthly"]] = None, start_month: Optional[str] = None, seed: Optional[str] = None, extra_keywords: Optional[List[str]] = None, trends: Optional[bool] = None, include_refreshes: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Plan the editorial calendar. Builds and stores an editorial calendar for the
        coming months at a cadence (weekly ≈ 4 a month, fortnightly 2, monthly 1, or a
        number a month) from the topic map (Search Console clusters with no strong page:
        write; clusters on page two: refresh), extraKeywords not yet covered, the
        keyword registry (a keyword another page owns becomes a refresh of that page,
        never a second page), and seasonality (stored monthly volumes; trends: true
        reads Google Trends for the top items, paid): seasonal pieces land two months
        before their peak, the rest in order of value. Each item carries its keyword and
        cluster, ready-made build_content_brief arguments, target URL, internal links to
        add (to and from), search volume, estimated monthly clicks at position 3 and
        their value (clicks × CPC). hubs lays each pillar with three or more clusters
        out as a hub — one pillar (2,500–4,000 words), 2–5 clusters of 2–4 spokes
        (1,200–1,800 words), templates by intent, a link matrix (spoke ↔ pillar
        mandatory, 2–3 spoke-to-spoke, at most one cross-cluster) — and scores the live
        site's links against it: no orphans, pillar links both ways, 80% of planned
        links present. Answers 'what should we publish over the next quarter'. Read back
        with list_content_plan; change items with update_content_plan_item. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("plan_content", _present({"clientId": client_id, "months": months, "cadence": cadence, "startMonth": start_month, "seed": seed, "extraKeywords": extra_keywords, "trends": trends, "includeRefreshes": include_refreshes, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def plan_redirect_map(self, *, client_id: str, new_crawl_id: Optional[str] = None, old_urls: Optional[List[str]] = None, old_sitemap_url: Optional[str] = None, old_crawl_id: Optional[str] = None, format_: Optional[Literal["json", "csv", "htaccess", "nginx"]] = None, min_confidence: Optional[float] = None, limit: Optional[int] = None) -> Any:
        """Redirect map for a migration. Proposes a 1:1 301 redirect for each old address
        of a site migration, onto the page of the new site's crawl (newCrawlId, default
        latest) that most plausibly replaced it, with a confidence (0–1) and the
        evidence: the new site already redirects it, the same path (also ignoring case,
        slashes and .html/.php), the same text, or similar path words, title and text;
        failing those the nearest surviving section, and only then the homepage
        (flagged: Google treats mass homepage redirects as soft 404s). Give exactly one
        old source: oldUrls (a list), oldSitemapUrl (the old site's sitemap) or
        oldCrawlId (an earlier crawl of this client — best, since titles and text are
        compared too). format csv, htaccess (exact-match RewriteRules) or nginx (a map
        block) returns the whole map as a file in content. Answers 'where should each
        old URL redirect'. Free."""
        return self.call("plan_redirect_map", _present({"clientId": client_id, "newCrawlId": new_crawl_id, "oldUrls": old_urls, "oldSitemapUrl": old_sitemap_url, "oldCrawlId": old_crawl_id, "format": format_, "minConfidence": min_confidence, "limit": limit}))

    def post_review_reply(self, *, client_id: str, location_id: str, review_id: str, reply: str) -> Any:
        """Post a reply to a Google review. Posts the owner's reply to one Google review —
        or replaces the reply already there — through the client's connected Business
        Profile, and records it as answered. Needs the listing connected under Local
        (the connection asks Google for permission to manage it); reviewId is from
        draft_review_replies or get_local_visibility. Answers 'post that reply'. Free."""
        return self.call("post_review_reply", _present({"clientId": client_id, "locationId": location_id, "reviewId": review_id, "reply": reply}))

    def preview_weekly_digest(self, *, client_id: str) -> Any:
        """This week's digest. The weekly digest for the client as it would be posted, for
        the last complete Monday-to-Sunday week (week; the title names its days): what
        changed in Search Console, revenue and AI assistant visits; why it probably
        changed (demand, rankings, or particular pages); and the top five actions — from
        striking distance, low click-through, decaying pages and the latest audit — with
        the extra monthly clicks each is estimated to bring and, where revenue or goal
        values allow, what they are worth. Audit findings accepted as intentional
        (accept_issue) are left out and counted in basis; with path owners set, each
        audit action names its owner and byOwner groups them. Answers 'what should we do
        this week and why'. Free."""
        return self.call("preview_weekly_digest", _present({"clientId": client_id}))

    def propose_keyword_owners(self, *, client_id: str, days: Optional[int] = None, limit: Optional[int] = None, seed: Optional[str] = None) -> Any:
        """Propose an owner page for each query cluster. Groups the client's non-branded
        Search Console queries by the page they land on most and proposes, for each
        cluster, the page Search Console sends the most clicks to (impressions when none
        has clicks): its share of the cluster's clicks, the other pages competing,
        whether it is already registered (and to which page), and confidence clear,
        split (the clicks are divided: cannibalization) or thin. Nothing is saved:
        accept with set_keyword_owners. Answers 'which page should own each topic'.
        Free."""
        return self.call("propose_keyword_owners", _present({"clientId": client_id, "days": days, "limit": limit, "seed": seed}))

    def push_tasks_to_tracker(self, *, client_id: str, provider: Literal["jira", "linear", "github"], task_ids: Optional[List[str]] = None, statuses: Optional[List[Literal["todo", "in_progress", "done", "wont_do"]]] = None, limit: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Mirror tasks into Jira, Linear or GitHub. Creates an issue in the client's
        connected Jira project, Linear team or GitHub repository for each task (the
        chosen taskIds, or every task of the chosen statuses — default the open ones),
        with the task's notes and what it is about, and links the two so status syncs
        both ways. Tasks already mirrored there are skipped. dryRun: true creates
        nothing and lists wouldCreate (each issue's title and description) and
        alreadyLinked. Pairs with create_tasks_from_audit. Answers 'put the audit into
        our Jira'. Connect the tracker first with connect_integration. Free."""
        return self.call("push_tasks_to_tracker", _present({"clientId": client_id, "provider": provider, "taskIds": task_ids, "statuses": statuses, "limit": limit, "dryRun": dry_run}))

    def query_data(self, *, client_id: str, dataset: Literal["gsc", "web_events", "crawl_pages", "crawl_issues", "crawl_links", "rank_captures", "backlinks", "revenue_orders", "web_agent_visits"], dimensions: Optional[List[str]] = None, metrics: Optional[List[str]] = None, columns: Optional[List[str]] = None, filters: Optional[List[Dict[str, Any]]] = None, from_: Optional[str] = None, to: Optional[str] = None, order_by: Optional[List[Dict[str, Any]]] = None, crawl_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Query the stored data. Asks any question of a client's stored data the other
        tools do not answer: pick a dataset (describe_datasets), group by dimensions,
        compute metrics (count, sum(col), avg(col), min, max, uniq, plus ctr and
        position for Search Console, visitors and visits for analytics), filter (eq,
        neq, contains, starts_with, gt, lt, in, regex), order and limit — or list rows
        with columns. Search Console can also be grouped or filtered by each query's
        intent, topic and branded flag. Answers 'which queries containing X lost clicks
        on mobile in Spain', 'how many 404s per template', 'how are commercial queries
        trending'. Read-only and always limited to the client's own data. Up to 10,000
        rows; export_data for more. Free."""
        return self.call("query_data", _present({"clientId": client_id, "dataset": dataset, "dimensions": dimensions, "metrics": metrics, "columns": columns, "filters": filters, "from": from_, "to": to, "orderBy": order_by, "crawlId": crawl_id, "limit": limit}))

    def query_keyword_list(self, *, list_id: str, text: Optional[str] = None, tags: Optional[List[str]] = None, untagged: Optional[bool] = None, intents: Optional[List[Literal["informational", "navigational", "commercial", "transactional"]]] = None, min_volume: Optional[int] = None, max_volume: Optional[int] = None, min_difficulty: Optional[int] = None, max_difficulty: Optional[int] = None, sort: Optional[Literal["term", "volume", "difficulty", "cpc", "added", "refreshed"]] = None, order: Optional[Literal["asc", "desc"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, format_: Optional[Literal["json", "csv"]] = None) -> Any:
        """Filter and sort a keyword list. One list's keywords with the metrics last read
        for each — volume, keyword difficulty, CPC (micro-USD), competition, intent,
        SERP features and when they were read — plus tags and notes, filtered by text,
        tags (all must match), untagged, intent and volume or difficulty ranges, and
        sorted by term, volume, difficulty, cpc, added or refreshed. Keywords with no
        metrics sort last. format: csv also returns the page as CSV for a spreadsheet.
        Answers 'which keywords on that list are easy and over 1,000 searches' and
        'export that list'. Metrics are null until refresh_keyword_list_metrics has run.
        Free."""
        return self.call("query_keyword_list", _present({"listId": list_id, "text": text, "tags": tags, "untagged": untagged, "intents": intents, "minVolume": min_volume, "maxVolume": max_volume, "minDifficulty": min_difficulty, "maxDifficulty": max_difficulty, "sort": sort, "order": order, "limit": limit, "offset": offset, "format": format_}))

    def queue_url_inspections(self, *, client_id: str, urls: List[str]) -> Any:
        """Queue URLs for Search Console inspection. Queues up to 500 of the client's URLs
        for Search Console's URL inspection, which runs in the background within
        Google's daily allowance. Answers 'check whether all these pages are indexed'.
        URLs that are not on the client's own site are refused and listed with the
        reason. Read the results with get_index_coverage as they arrive; inspect_url
        checks one URL immediately. Needs Search Console connected (see
        get_connection_link)."""
        return self.call("queue_url_inspections", _present({"clientId": client_id, "urls": urls}))

    def recheck_links(self, *, client_id: str, render: Optional[bool] = None, source_urls: Optional[List[str]] = None) -> Any:
        """Re-check the pages that link to a client. Sends our crawler to the pages said to
        link to the client to see whether each still does — slowly and politely, so it
        takes a while; read the result with get_link_checks. A second request within the
        hour lands on the check already running. render: true instead reads, in a real
        browser, the pages the last check marked unverifiable_js (app shells whose links
        JavaScript draws) — or the sourceUrls given, if the link checks know them — up
        to 25 a run, and re-judges each link as live, lost or moved (a page that draws
        nothing even in the browser stays unverifiable_js, and one that will not load
        keeps its verdict); it runs in the background, so poll get_run_status with job
        'links' and the runId, then read get_link_checks (rendered: true on those
        pages). No vendor charge, but it visits other people's sites on the client's
        behalf, so it needs client:manage. Refused when the client has no rank tracker
        yet (HTML) or no page is waiting on a browser (render: nothing_to_render).
        Answers 'check our links again' and 'check the JavaScript pages properly'."""
        return self.call("recheck_links", _present({"clientId": client_id, "render": render, "sourceUrls": source_urls}))

    def record_order(self, *, client_id: str, order_id: str, amount_minor: int, currency: str, at: str, visit: Optional[str] = None, refund_of: Optional[str] = None, customer_id: Optional[str] = None) -> Any:
        """Record an order (no store connected). Records one order for a business not on
        Stripe, Shopify or Paddle, so get_seo_revenue counts it: orderId (the site's
        own; recording it again replaces it, a replay is answered 'unchanged'),
        amountMinor in the currency's minor unit (4999 = 49.99 USD), currency, at (when
        paid) and, when the site kept one, visit — the visit token /api/collect gave its
        server collector while the buyer was on the site, which credits the order to
        that visit's landing page, source and channel. A refund is an order of its own
        with refundOf naming the order it refunds. Answers 'log this crypto payment
        against the visit it came from'. Free."""
        return self.call("record_order", _present({"clientId": client_id, "orderId": order_id, "amountMinor": amount_minor, "currency": currency, "at": at, "visit": visit, "refundOf": refund_of, "customerId": customer_id}))

    def record_orders(self, *, client_id: str, orders: List[Dict[str, Any]]) -> Any:
        """Record orders in a batch. record_order for up to 500 orders in one call, for a
        server pushing its orders (POST /api/v1/tools/record_orders with an
        Idempotency-Key). Each is answered on its own — recorded, updated, unchanged or
        refused with the reason — and one refused order does not stop the rest. Refunds
        may refer to orders earlier in the same batch. Answers 'send last night's orders
        in one request'. Free."""
        return self.call("record_orders", _present({"clientId": client_id, "orders": orders}))

    def refresh_domain_data(self, *, client_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Refresh domain and backlink data now. Refreshes everything bought about the
        client's domain — overview, ranked keywords, competitors, top pages and the
        backlink profile — plus what up to five tracked competitors rank for and who
        links to them. Answers 'update the backlinks and keyword data'. The dearest
        thing the product does: quote it with estimate_cost first; with maxCostMicros
        the refresh is refused before it starts when its estimate is over the limit.
        Runs in the background for a few minutes: poll get_run_status with job 'domain'.
        A second request within the hour lands on the refresh already going. Can spend:
        pass max_cost_micros to cap it."""
        return self.call("refresh_domain_data", _present({"clientId": client_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def refresh_keyword_list_metrics(self, *, client_id: str, list_id: str, only_older_than_days: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Refresh a keyword list's metrics. Re-reads volume, keyword difficulty, CPC,
        competition, intent and SERP features for every Google keyword on a list from
        DataForSEO Labs, in bulk (one read per market per 700 keywords), and stores them
        on the list. Answers 'update the numbers on that list'. onlyOlderThanDays skips
        keywords refreshed more recently, so a big list is not bought twice in a week.
        Keywords for other engines, or markets the research index does not cover, are
        skipped with the reason; terms the index has nothing for are listed in noData
        and their old figures cleared. clientId is the account billed: a client's list
        is refreshed under its own client, an agency list under any client the caller
        names. A paid lookup unless anyone read the same thing recently; quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("refresh_keyword_list_metrics", _present({"clientId": client_id, "listId": list_id, "onlyOlderThanDays": only_older_than_days, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def refresh_rankings(self, *, client_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Capture rankings now. Captures the client's rank tracker now instead of at its
        next scheduled run: every tracked keyword on every device the tracker reads,
        each a paid lookup. Answers 'get me today's positions'. Quote it with
        estimate_cost first; with maxCostMicros the run is refused before it starts when
        its estimate is over the limit. Runs in the background: poll get_run_status with
        job 'rank', then read get_rank_history or get_rank_summary. A second request
        within the same minute lands on the run already going rather than paying twice.
        Can spend: pass max_cost_micros to cap it."""
        return self.call("refresh_rankings", _present({"clientId": client_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def remove_annotations(self, *, client_id: str, ids: List[str]) -> Any:
        """Remove timeline notes. Removes the client's timeline notes by id; unknown ids
        are ignored. Answers 'take that note off'. Google's updates cannot be removed.
        Free."""
        return self.call("remove_annotations", _present({"clientId": client_id, "ids": ids}))

    def remove_client_facts(self, *, client_id: str, keys: List[str]) -> Any:
        """Remove facts from the registry. Removes the client's facts by key; unknown keys
        are ignored. Answers 'forget the old enterprise price'. Free."""
        return self.call("remove_client_facts", _present({"clientId": client_id, "keys": keys}))

    def remove_competitors(self, *, client_id: str, tracker_id: str, domains: List[str]) -> Any:
        """Remove competitors from a tracker. Stops measuring the named competitor domains
        on a rank tracker. Answers 'we no longer compete with this site'. Returns the
        tracker's remaining competitors. Naming a domain that is not on the list is not
        an error."""
        return self.call("remove_competitors", _present({"clientId": client_id, "trackerId": tracker_id, "domains": domains}))

    def remove_keyword_owners(self, *, client_id: str, keywords: List[str]) -> Any:
        """Release keywords from the registry. Removes the registry's claims on the given
        keywords; unknown keywords are ignored. Answers 'that keyword no longer belongs
        to that page'. Free."""
        return self.call("remove_keyword_owners", _present({"clientId": client_id, "keywords": keywords}))

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

    def remove_vendor_credential(self, *, provider: Literal["dataforseo", "serpapi", "anthropic", "bingwebmaster", "reportwebhook", "serpproxy", "googleads", "crux", "chatgpt", "gemini", "perplexity", "grok", "meta-ai", "deepseek", "pagespeed", "telegram", "naversearchad", "knowledgegraph", "webrisk"]) -> Any:
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

    def replay_webhooks(self, *, webhook_id: str, since: Optional[str] = None, delivery_id: Optional[str] = None) -> Any:
        """Send events again. Queues events for a webhook again: one delivery (deliveryId),
        or every subscribed event since an ISO time (default: the last 24 hours). For a
        receiver that was down. Answers 'resend what we missed'. Free."""
        return self.call("replay_webhooks", _present({"webhookId": webhook_id, "since": since, "deliveryId": delivery_id}))

    def research_topic(self, *, client_id: str, seed: str, limit: Optional[int] = None, serp: Optional[bool] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Subtopics, questions and headlines around a seed. Maps a topic: related keywords
        and keyword suggestions for a seed, with volume, difficulty and search intent,
        grouped into subtopics by the word they add to the seed; the questions people
        ask (People Also Ask and question keywords); and the headlines ranking now.
        Answers 'what should we write about around this topic'. Paid DataForSEO Labs
        reads and one results page on the client's account, each free when anyone read
        it lately. Can spend: pass max_cost_micros to cap it."""
        return self.call("research_topic", _present({"clientId": client_id, "seed": seed, "limit": limit, "serp": serp, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def resend_team_invite(self, *, invite_id: str) -> Any:
        """Resend an invite. Sends an invite again with a new link and a fresh 7 days; the
        old link stops working. By the inviteId list_team_invites gives. At most 5 sends
        per invite and one a minute. Answers 'they never got the email'."""
        return self.call("resend_team_invite", _present({"inviteId": invite_id}))

    def restore_client(self, *, client_id: str) -> Any:
        """Restore an archived client. Brings an archived client back: it is listed,
        tracked, crawled and reported on again, with its history as it was, and counts
        against the plan once more (refused when the plan's client limit is reached).
        Answers 'we're working with them again'. Safe to repeat: restored is false when
        the client was not archived."""
        return self.call("restore_client", _present({"clientId": client_id}))

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

    def revoke_log_source(self, *, client_id: str, source_id: str) -> Any:
        """Disconnect a log feed. Stops a log feed: its ingest URL refuses deliveries from
        now on, and an S3 source stops being pulled and its keys are deleted. Stored
        requests stay. Answers 'disconnect that log drain'. Free."""
        return self.call("revoke_log_source", _present({"clientId": client_id, "sourceId": source_id}))

    def revoke_portal_link(self, *, client_id: str, link_id: str) -> Any:
        """Revoke a client portal link. Stops a portal link working, immediately and for
        good. Answers 'that link was forwarded' or 'the engagement ended'. A link that
        is already revoked, or is not this client's, is refused rather than reported as
        done."""
        return self.call("revoke_portal_link", _present({"clientId": client_id, "linkId": link_id}))

    def revoke_report_link(self, *, link_id: str) -> Any:
        """Turn off one report link. Stops one link made with create_report_link (linkId
        from list_report_links or from create_report_link's answer) at once, leaving the
        report's other links working. Answers 'I sent the report link to the wrong
        person'. Revoking a link twice keeps the first time. Free."""
        return self.call("revoke_report_link", _present({"linkId": link_id}))

    def revoke_report_links(self, *, client_id: str, report_id: str) -> Any:
        """Turn off a report's links. Stops every link made so far with create_report_link
        for one saved report, at once. Answers 'turn off all the links to this report'.
        To stop one link and keep the rest, revoke_report_link. Links made afterwards
        work as normal. Free."""
        return self.call("revoke_report_links", _present({"clientId": client_id, "reportId": report_id}))

    def revoke_team_invite(self, *, invite_id: str) -> Any:
        """Withdraw an invite. Withdraws an invite so its link no longer works. Answers
        'cancel the invite to sam@'. Safe to repeat: revoked is false when it was
        already used or withdrawn."""
        return self.call("revoke_team_invite", _present({"inviteId": invite_id}))

    def rewrite_section(self, *, client_id: str, keyword: str, section: str, mode: Optional[Literal["rewrite", "extend"]] = None, missing_terms: Optional[List[str]] = None, questions: Optional[List[str]] = None, draft: Optional[str] = None, url: Optional[str] = None, instructions: Optional[str] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Rewrite a section to cover what is missing. Rewrites (mode rewrite) or extends
        (mode extend) one section of a page so it covers the terms, entities and
        questions the content score finds missing, keeping the section's own voice and
        the client's. Give missingTerms and questions yourself, or the whole draft
        (draft as Markdown, or url) to have them taken from a fresh score_content run.
        Returns the new Markdown and which asked-for terms it now uses and still misses,
        as we count them. Answers 'work these terms into this section'. A paid Claude
        call; scoring a draft also costs what score_content does. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("rewrite_section", _present({"clientId": client_id, "keyword": keyword, "section": section, "mode": mode, "missingTerms": missing_terms, "questions": questions, "draft": draft, "url": url, "instructions": instructions, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def run_ai_visibility_check(self, *, client_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Run an AI visibility check now. Asks every tracked question on the chosen
        assistants now, in the background; results arrive within minutes in
        get_ai_visibility_runs and get_ai_visibility_results. The schedule is unchanged.
        With maxCostMicros, the check is refused before it starts when its estimate is
        over the limit. Get the user's go-ahead first: it spends. Answers 'check it
        now'. Can spend: pass max_cost_micros to cap it."""
        return self.call("run_ai_visibility_check", _present({"clientId": client_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def run_audit_performance_sample(self, *, client_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Measure the audit's speed again. Takes the latest complete audit's speed sample
        again, in the background: a Lighthouse run (mobile) of the homepage and one page
        of each of the largest URL templates (up to 5 pages), and the origin's Chrome UX
        Report reading for phone and desktop — the same sample an audit takes when it
        finishes, replacing that audit's figures. For an audit that finished before a
        PageSpeed Insights key was connected, or whose runs failed. Takes a few minutes;
        read the result with get_audit_performance. Uses the agency's PageSpeed Insights
        and Chrome UX Report connections. Answers 'measure the site's speed now'. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("run_audit_performance_sample", _present({"clientId": client_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def run_data_sync_now(self, *, client_id: str, sync_id: str) -> Any:
        """Run a data sync now. Runs one sync immediately, outside its schedule, and says
        how many rows were written. Answers 'refresh the sheet now'. Free."""
        return self.call("run_data_sync_now", _present({"clientId": client_id, "syncId": sync_id}))

    def run_local_grid_scan(self, *, client_id: str, location_id: str, term: str, size: Optional[float] = None, spacing_km: Optional[float] = None, device: Optional[Literal["desktop", "mobile"]] = None, more_terms: Optional[List[str]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Run a map-pack grid scan. Searches the term at every point of a size × size grid
        around the location (spacingKm apart, 1.5 by default — 0.5 for a dense city
        centre, 5 for a rural area) and records where the business appears in the map
        pack. Sizes 3, 5, 7, 9 (suburban or a wide service area) and 13 (rural or a
        large metro); device mobile asks as a phone, which sees a different pack;
        moreTerms (up to two) scans other terms on the same grid — the service, the
        brand with the town, a long-tail query — each its own scan. Every point of every
        term is a paid lookup, so a 7 × 7 grid is 49 lookups and 13 × 13 is 169: quote
        it with estimate_cost and get the user's go-ahead first. Runs in the background;
        read the result with get_local_visibility a few minutes later. With
        maxCostMicros, the scan is refused before it starts when its estimate is over
        the limit. Answers 'scan our map-pack visibility now'. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("run_local_grid_scan", _present({"clientId": client_id, "locationId": location_id, "term": term, "size": size, "spacingKm": spacing_km, "device": device, "moreTerms": more_terms, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def save_ai_visibility_setup(self, *, client_id: str, add_prompts: Optional[List[Dict[str, Any]]] = None, update_prompts: Optional[List[Dict[str, Any]]] = None, retire_prompt_ids: Optional[List[str]] = None, add_brands: Optional[List[Dict[str, Any]]] = None, dry_run: Optional[bool] = None) -> Any:
        """Change what AI visibility tracks. Adds questions (each optionally with a
        two-letter market, a topic, and branded true/false to override the automatic
        reading), regroups or reclassifies questions by id (updatePrompts: topic null to
        ungroup, branded null to go back to automatic), retires questions by id (past
        answers keep their question), and adds brands to look for (name, domain,
        aliases; isClient for the client's own — there should be exactly one). Questions
        already tracked are skipped. dryRun: true changes nothing and lists what would:
        the questions it would add, retire and regroup, those it would skip, and the
        brands it would add (with why one would be refused). Write questions the way a
        buyer would ask an assistant, without naming any brand; suggest_ai_prompts
        drafts them. Answers 'track these questions'. Free; the checks that follow are
        what cost."""
        return self.call("save_ai_visibility_setup", _present({"clientId": client_id, "addPrompts": add_prompts, "updatePrompts": update_prompts, "retirePromptIds": retire_prompt_ids, "addBrands": add_brands, "dryRun": dry_run}))

    def save_baidu_token(self, *, client_id: str, site_url: str, token: str) -> Any:
        """Save the client's Baidu push token. Saves the link-push token from Baidu Ziyuan
        (ziyuan.baidu.com, link submission page) for the client's site, so
        submit_baidu_urls can push pages. Answers 'connect Baidu for this client'. The
        site must be the client's own registered site; the token is stored encrypted and
        never returned. Replaces any token already saved."""
        return self.call("save_baidu_token", _present({"clientId": client_id, "siteUrl": site_url, "token": token}))

    def save_disavow_file(self, *, client_id: str, entries: List[Dict[str, Any]]) -> Any:
        """Build, keep and compare a disavow file. Builds a Google disavow file for the
        client from domains and URLs (as build_disavow_file does), keeps it in the
        client's disavow history, and says what changed against the previous saved file:
        domains and URLs added and dropped. Nothing is submitted — Google takes the file
        by upload in Search Console, which a person does after reviewing every line.
        Answers 'make this month's disavow file and show what changed'. Free."""
        return self.call("save_disavow_file", _present({"clientId": client_id, "entries": entries}))

    def save_report_template(self, *, name: str, sections: List[Dict[str, Any]], template_id: Optional[str] = None, client_id: Optional[str] = None, description: Optional[str] = None, audience: Optional[str] = None, tone: Optional[str] = None, sign_off: Optional[str] = None) -> Any:
        """Save a report template. Saves a reusable brief for a kind of report: a name, who
        it is for, sections in order (each with a line on what goes under it), tone and
        sign-off. Answers 'make this our monthly report format'. Without clientId it is
        agency-wide, which only someone who sees every client may change; with one it is
        that client's own. Without templateId a new template is made; with one, it is
        replaced. Only save a template when the user asks for one — a one-off report
        needs none. Free."""
        return self.call("save_report_template", _present({"templateId": template_id, "clientId": client_id, "name": name, "description": description, "audience": audience, "sections": sections, "tone": tone, "signOff": sign_off}))

    def save_vendor_credential(self, *, provider: Literal["dataforseo", "serpapi", "anthropic", "bingwebmaster", "reportwebhook", "serpproxy", "googleads", "crux", "chatgpt", "gemini", "perplexity", "grok", "meta-ai", "deepseek", "pagespeed", "telegram", "naversearchad", "knowledgegraph", "webrisk"], secret: str, login: Optional[str] = None, google_ads: Optional[Dict[str, Any]] = None) -> Any:
        """Connect a vendor account. Stores the agency's own account for a data vendor or
        AI assistant — DataForSEO (the API login and API password, or leave login out
        and pass the Base64 login:password DataForSEO's panel shows as secret; the check
        also confirms the account is verified), SerpApi, a proxy pool (serpproxy: one
        URL per line), Google Ads (six values in googleAds), an Anthropic, OpenAI,
        Gemini or Perplexity key, and the rest get_vendor_connections names — and checks
        it works straight away with one free call. Answers 'connect our DataForSEO
        account'. A failed check gives errorCode (vendor_credentials_rejected,
        vendor_account_unverified, vendor_balance_empty, vendor_product_not_enabled) and
        next, the step that fixes it. Replaces any key already saved for that vendor.
        The response says whether the check passed; it never contains the key."""
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

    def schedule_weekly_digest(self, *, client_id: str, provider: Literal["slack", "discord", "telegram"], weekday: Optional[int] = None, run_hour: Optional[int] = None, paused: Optional[bool] = None) -> Any:
        """Post the weekly digest to a chat. Posts the weekly digest (see
        preview_weekly_digest) to the client's connected Slack, Discord or Telegram
        every week on a weekday (0 Sunday – 6 Saturday, default Monday) at a UTC hour.
        One schedule per chat connection; calling again changes it. Answers 'send Acme's
        weekly digest to their Slack on Mondays'."""
        return self.call("schedule_weekly_digest", _present({"clientId": client_id, "provider": provider, "weekday": weekday, "runHour": run_hour, "paused": paused}))

    def score_amazon_listing(self, *, client_id: str, asin: str, keyword: str, location_code: Optional[int] = None, language_code: Optional[str] = None, competitors: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Score an Amazon listing against the top results. Reads an Amazon product (by
        ASIN) and the listings ranking for a keyword, and scores the listing: title
        length and whether it carries the keyword, the bullet points (count and length),
        images, the terms the top titles share that this one lacks, and its rating,
        ratings count and price against the top listings' median. Each check pass, warn
        or fail with the reason. Answers 'how does our Amazon listing compare' and 'what
        should our title say'. Two reads from DataForSEO's Amazon data. A paid lookup on
        the client's account (spend says how much); quote it with estimate_cost. Can
        spend: pass max_cost_micros to cap it."""
        return self.call("score_amazon_listing", _present({"clientId": client_id, "asin": asin, "keyword": keyword, "locationCode": location_code, "languageCode": language_code, "competitors": competitors, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def score_app_metadata(self, *, client_id: str, store: Literal["app_store", "google_play"], app_id: str, keywords: Optional[List[str]] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, task_id: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Score an app's store listing. Scores an App Store or Google Play listing for
        search: the title's length and whether it carries the target keywords, the
        subtitle (App Store) or short description (Play), the description's length and
        keyword use, screenshots, rating, ratings count and how recently it was updated
        — each pass, warn or fail with the reason — and, per keyword, where the listing
        uses it. App Store listings are read from Apple's free lookup API; a Play
        listing is read through DataForSEO's App Data, which queues the read: when it is
        not back within half a minute the answer is pending with a taskId to pass again.
        Answers 'how good is our app listing' and 'is our keyword in the title'. App
        Store: free. Google Play: A paid lookup on the client's account (spend says how
        much); quote it with estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("score_app_metadata", _present({"clientId": client_id, "store": store, "appId": app_id, "keywords": keywords, "locationCode": location_code, "languageCode": language_code, "taskId": task_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def score_content(self, *, client_id: str, keyword: str, url: Optional[str] = None, html: Optional[str] = None, markdown: Optional[str] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Score a draft before publishing. Scores a draft (a URL, HTML or Markdown) 0–100
        against the pages that rank for its keyword: term coverage, outline coverage,
        questions answered, length and structure — with the missing terms (and how often
        to use them), missing sections, unanswered questions and a fix list, most
        important first — factConflicts, sentences stating a price, limit or date that
        contradicts the client's registered facts; uncitedClaims, the percentages, money
        and large numbers, 'according to X', 'by 2030' and '3x' figures with no link,
        footnote or source line within 200 characters (uncitedRatio, a warning above
        0.4; a heuristic); invisibleChars, zero-width, bidi and tag characters by
        codepoint; draftQuality, which only detects and never rewrites: 26 filler and 46
        stock AI phrases scored per 1,000 tokens, information density, bigram
        repetition, flags (filler 50+, AI phrasing 40+, density under 0.20, repetition
        30+, under 300 tokens) and a weighted overall; and placement, the keyword in the
        first 100 words, the URL slug and the front of the title, heading stuffing (more
        than two subheadings repeating it), average sentence length against 15–20 words,
        internal links per 1,000 words against 3–5, and a table of contents on pages of
        1,500 words or more. Answers 'is this ready to publish' and 'what should I add'.
        Run it after each revision until it is at par with the results page. Same cost
        as get_serp_content_profile; a results page bought for the brief is reused free
        for a day. Can spend: pass max_cost_micros to cap it."""
        return self.call("score_content", _present({"clientId": client_id, "keyword": keyword, "url": url, "html": html, "markdown": markdown, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def score_eeat(self, *, client_id: str, urls: Optional[List[str]] = None, top_pages: Optional[int] = None, judge: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Score pages for E-E-A-T. Scores pages of the client's site (urls, up to 20, or
        the topPages by Search Console clicks) for Experience (20), Expertise (25),
        Authoritativeness (25) and Trust (30), each from sub-criteria graded Strong,
        Moderate, Weak or None with the evidence and the fix: first-hand method and
        results, figures, original images, a byline and author page, Person markup with
        jobTitle and sameAs, credentials, citations to outside and primary sources and
        the share of uncited claims, visible dates, about, contact, privacy and terms
        pages, HTTPS, reviews, a returns policy on shops, specialised vocabulary, awards
        and accreditations, 'featured in' media coverage, professional affiliations, a
        history of publishing on the topic (other crawled pages on it), visible
        corrections and update history, no deceptive practices (undisclosed affiliate
        links, clickbait headlines, false urgency), secure payments on shops, and for
        the site referring domains and brand mentions from our index and a Wikidata
        entity. Flags pages weak on who, how and why (atRisk), YMYL pages (health,
        finance, legal, news, civic, groups) with no credentials (Expertise capped at
        Weak), generic AI-style pages (one heading template, no author, stock phrasing),
        stale pages on fast-moving topics, and reading ease outside 60–70 (information
        only). Bands at 90/70/50/30, each page and the sample with the next steps for
        its band. A heuristic. judge: true regrades Experience with one metered Claude
        call (quote it with estimate_cost). Answers 'does our content show E-E-A-T' and
        'which pages look untrustworthy'. Free without judge. Can spend: pass
        max_cost_micros to cap it."""
        return self.call("score_eeat", _present({"clientId": client_id, "urls": urls, "topPages": top_pages, "judge": judge, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def search_local_businesses(self, *, client_id: str, lat: float, lng: float, radius_km: Optional[float] = None, categories: Optional[List[str]] = None, name: Optional[str] = None, min_rating: Optional[float] = None, claimed: Optional[bool] = None, limit: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Businesses in an area. Every Google Maps business within a radius of a point, by
        category and/or name, with rating, reviews, claimed status, photos, site and ids
        — up to 1,000. Answers 'who are all the plumbers within 10 km' and 'which rivals
        have unclaimed listings'. Category names are Google's (dentist, plumber,
        pizza_restaurant); get_local_categories lists those in an area. A paid lookup on
        the client's account unless anyone read the same thing recently; quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("search_local_businesses", _present({"clientId": client_id, "lat": lat, "lng": lng, "radiusKm": radius_km, "categories": categories, "name": name, "minRating": min_rating, "claimed": claimed, "limit": limit, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def search_locations(self, *, client_id: str, query: str, country: Optional[str] = None, type_: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Find a location to track from. Looks up search locations in a country by name —
        cities, counties, regions, DMAs, postal areas — with the location code
        create_rank_tracker and the research tools take. Answers 'track us from
        Manchester, not all of the UK'. Free."""
        return self.call("search_locations", _present({"clientId": client_id, "query": query, "country": country, "type": type_, "limit": limit}))

    def search_web_content(self, *, client_id: str, keyword: str, exact: Optional[bool] = None, in_title: Optional[bool] = None, page_types: Optional[List[Literal["ecommerce", "news", "blogs", "message-boards", "organization"]]] = None, sentiment: Optional[Literal["positive", "negative", "neutral"]] = None, since: Optional[str] = None, min_domain_rank: Optional[int] = None, exclude_domain: Optional[str] = None, one_per_domain: Optional[bool] = None, sort: Optional[Literal["relevance", "newest", "domain_rank"]] = None, summary: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Pages on the web that mention a phrase. Content Explorer over DataForSEO's
        content index: pages that mention a word or phrase, each with its domain, title,
        snippet, publish date, domain rank (0–1000), sentiment (positive, negative,
        neutral) and page type, filtered by page type, sentiment, date and domain rank,
        and a summary of the whole set — sentiment split, top domains, page types.
        Answers 'who writes about this', 'who mentions our brand without linking', 'what
        is said about this topic, and how warmly' and 'which blogs cover this niche'. A
        paid lookup on the client's account unless anyone read the same thing recently
        (spend says which); quote it with estimate_cost. Can spend: pass max_cost_micros
        to cap it."""
        return self.call("search_web_content", _present({"clientId": client_id, "keyword": keyword, "exact": exact, "inTitle": in_title, "pageTypes": page_types, "sentiment": sentiment, "since": since, "minDomainRank": min_domain_rank, "excludeDomain": exclude_domain, "onePerDomain": one_per_domain, "sort": sort, "summary": summary, "limit": limit, "offset": offset, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def send_outreach(self, *, client_id: str, mailbox_id: str, prospects: List[Dict[str, Any]], sequence_id: Optional[str] = None, dry_run: Optional[bool] = None) -> Any:
        """Send outreach emails from a connected mailbox. Sends the first email to each
        prospect from the chosen mailbox now, and schedules the sequence's follow-ups
        (when a sequenceId is given), which the hourly sweep sends unless a reply
        arrives first. Each prospect takes its own subject and body (from
        draft_outreach_emails, say) or the sequence's first step; the address is to, or
        the contact saved on the prospect. A prospect with no address, or already
        contacted, is skipped and listed. Sent prospects move to contacted. This sends
        real email from a person's mailbox: confirm the list and the wording with the
        user first — dryRun: true sends nothing and returns wouldSend, every email
        (address, subject, body) and follow-up (with when it would go) exactly as it
        would be sent. Answers 'send these outreach emails'. No vendor charge."""
        return self.call("send_outreach", _present({"clientId": client_id, "mailboxId": mailbox_id, "sequenceId": sequence_id, "prospects": prospects, "dryRun": dry_run}))

    def send_report(self, *, client_id: str, report_id: str, idempotency_key: Optional[str] = None) -> Any:
        """Send a report now. Sends a saved report to its scheduled recipients now,
        covering the month just gone. Answers 'send the report'. Recipients come from
        the report's schedule and cannot be named here. Pass an idempotencyKey to make a
        retry land on the same send instead of emailing the client twice."""
        return self.call("send_report", _present({"clientId": client_id, "reportId": report_id, "idempotencyKey": idempotency_key}))

    def send_test_event(self, *, webhook_id: str) -> Any:
        """Send a test event. Queues an alert.fired test event to one webhook, delivered
        within a minute, so a receiver's signature check can be tried end to end.
        Answers 'test my webhook'. Free."""
        return self.call("send_test_event", _present({"webhookId": webhook_id}))

    def send_weekly_digest_now(self, *, client_id: str, provider: Literal["slack", "discord", "telegram"]) -> Any:
        """Post the digest now. Builds this week's digest and posts it to the client's
        connected Slack, Discord or Telegram straight away, outside any schedule.
        Answers 'send the digest to the channel now'."""
        return self.call("send_weekly_digest_now", _present({"clientId": client_id, "provider": provider}))

    def serp_overview(self, *, client_id: str, term: str, location_code: Optional[int] = None, language_code: Optional[str] = None, refresh: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Who is on the first page for a keyword. The current top ten organic results for
        a keyword, each with domain authority, referring domains, the estimated organic
        traffic of that page, links into the page where counted, and every feature on
        the results page — plus why the keyword's difficulty is what it is. Answers
        'could we get onto that page, and who would we have to beat'. Read from a recent
        capture when one is held, bought otherwise. Each figure says where it came from
        (our link graph or the vendor; panel or published click curve), and anything
        unknown is null, never zero. Can spend: pass max_cost_micros to cap it."""
        return self.call("serp_overview", _present({"clientId": client_id, "term": term, "locationCode": location_code, "languageCode": language_code, "refresh": refresh, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def set_ai_visibility_schedule(self, *, client_id: str, cadence: Optional[Literal["off", "daily", "weekly", "monthly"]] = None, engines: Optional[List[Literal["claude", "chatgpt", "gemini", "perplexity", "google-aio", "copilot", "google-ai-mode", "grok", "meta-ai", "deepseek"]]] = None, sentiment: Optional[bool] = None) -> Any:
        """Set how often AI visibility is checked. Sets a client's cadence (off, daily,
        weekly or monthly; weekly unless changed) which assistants it is checked on
        (engines; null or empty for every one the agency has configured), and whether
        each answer naming a tracked brand is also judged for sentiment (off by default;
        one metered Claude call per such answer, its ceiling in
        estimate_ai_visibility_cost as sentimentIfOnPerRunMaxMicros). Every scheduled
        check asks every question on every chosen assistant, so show
        estimate_ai_visibility_cost first. Answers 'check this daily on ChatGPT and
        Perplexity'. Free to set."""
        return self.call("set_ai_visibility_schedule", _present({"clientId": client_id, "cadence": cadence, "engines": engines, "sentiment": sentiment}))

    def set_branding(self, *, name: str, logo_url: str, primary_color: str) -> Any:
        """Set the agency's branding. Renames the agency and sets the logo and colour on
        its reports and portal links. Answers 'put our logo on the reports'. The logo
        must be an https:// address and the colour six-digit hex such as #1f5ad6; empty
        strings clear them. Send all three: this replaces what is there."""
        return self.call("set_branding", _present({"name": name, "logoUrl": logo_url, "primaryColor": primary_color}))

    def set_budget(self, *, client_id: str, monthly_usd: Optional[float] = None, alert_at: Optional[float] = None) -> Any:
        """Set a client's monthly budget and alert. Sets a client's monthly spending budget
        in USD (null removes it; paid calls past it are refused) and the share of it,
        0–1, at which a budget.threshold event and alert fire once that month (null
        turns the alert off). Leave either out to keep it. A per-call ceiling belongs to
        an API key: create_api_key's maxCostUsdPerCall. Answers 'cap this client at $50
        a month and warn me at 80%'. Free."""
        return self.call("set_budget", _present({"clientId": client_id, "monthlyUsd": monthly_usd, "alertAt": alert_at}))

    def set_client_facts(self, *, client_id: str, facts: List[Dict[str, Any]], dry_run: Optional[bool] = None) -> Any:
        """Record the client's canonical facts. Writes the client's facts — prices, plan
        limits, countries served, founding date, contact details — each with a key
        ("starter plan price"), its value ("$29/month"), a category and optionally the
        terms a sentence must contain to be about it; replaces a fact with the same key.
        dryRun: true saves nothing and lists wouldSet, each fact as it would be saved
        with the value it would replace. check_ai_brand_accuracy checks assistants
        against them first, and score_content and get_freshness_queue flag pages whose
        text contradicts one. Answers 'remember that our price is now $29'. Free."""
        return self.call("set_client_facts", _present({"clientId": client_id, "facts": facts, "dryRun": dry_run}))

    def set_crawl_auth(self, *, client_id: str, basic_auth: Optional[Dict[str, Any]] = None, headers: Optional[List[Dict[str, Any]]] = None, cookies: Optional[str] = None, clear: Optional[bool] = None) -> Any:
        """Credentials for crawling a staging site. Lets the crawler into a staging or
        password-protected site: HTTP basic auth (username and password), custom request
        headers (e.g. a bypass token for a firewall, up to 10) and cookies ('name=value;
        other=value'). Replaces whatever was set; clear: true removes it all. Stored
        encrypted, sent only to the client's own domain (never to a redirect elsewhere
        or a third-party script), and never shown again — get_crawl_settings lists only
        the username and header and cookie names. Answers 'audit our staging site' and
        'crawl behind the login'. Free."""
        return self.call("set_crawl_auth", _present({"clientId": client_id, "basicAuth": basic_auth, "headers": headers, "cookies": cookies, "clear": clear}))

    def set_crawl_schedule(self, *, client_id: str, cadence: Literal["off", "daily", "weekly", "monthly"], day: Optional[int] = None, hour: Optional[int] = None) -> Any:
        """Set when the site is crawled. Sets how often the client's site is crawled
        without anyone asking: off, daily, weekly or monthly; weekly on Monday at 02:00
        UTC unless changed. day is the weekday for weekly (0 Sunday to 6 Saturday;
        default 1, Monday) or the day of the month for monthly (1–28; default 1); hour
        is the UTC hour (default 2). Scheduled crawls use the client's crawl settings
        and wait their turn in the crawl queue like any other; one is never started
        while another crawl of the site is running, and a crawl started by hand since
        the last slot counts as that slot's. get_crawl_settings shows the schedule and
        when it next runs. Answers 'crawl this site every night'. Free."""
        return self.call("set_crawl_schedule", _present({"clientId": client_id, "cadence": cadence, "day": day, "hour": hour}))

    def set_crawl_settings(self, *, client_id: str, strip_params: Optional[List[str]] = None, extractions: Optional[List[Dict[str, Any]]] = None, render: Optional[Literal["off", "shells", "all"]] = None, render_max_pages: Optional[int] = None, mode: Optional[Literal["spider", "list", "sitemap"]] = None, list_urls: Optional[List[str]] = None, include_patterns: Optional[List[str]] = None, exclude_patterns: Optional[List[str]] = None, user_agent: Optional[Dict[str, Any]] = None, requests_per_second: Optional[float] = None, concurrency: Optional[int] = None, max_depth: Optional[int] = None, max_pages: Optional[int] = None) -> Any:
        """Change how the site is crawled. Changes the client's crawl settings for the next
        crawl; fields left out are kept. mode: spider (follow links from the home page
        and sitemap), list (crawl only listUrls, up to 5,000 addresses on the client's
        domain) or sitemap (crawl only the sitemap's URLs). includePatterns /
        excludePatterns: wildcards on the path and query ('/blog/*', '*?sort=*',
        '/*.pdf') or full addresses — with includes set, only matching URLs are crawled
        (the home page is still read to find them). maxPages (up to 20,000) and maxDepth
        (clicks from the start, up to 50). userAgent: preset seolyticize (default),
        googlebot-smartphone, googlebot-desktop, bingbot, chrome, or custom with your
        own string; robots.txt is obeyed as that crawler. requestsPerSecond (0.2–10,
        default 4) and concurrency (1–5); the crawler still backs off on 429s, 5xx and
        Retry-After. For staging sites' passwords, headers and cookies use
        set_crawl_auth. stripParams removes query parameters from every discovered URL
        (names, or prefixes like utm_*), so sorted and filtered copies of a page are
        crawled once. extractions reads values off every page (up to 10): css (a
        selector, optionally an attribute), xpath (//div[@class='author'],
        //meta[@property='og:type']/@content, (//a)[1]/@href — child and descendant
        steps, attribute and text tests, positions), regex (first group), jsonld
        ('Article.datePublished') or meta (a name or property) — see
        get_extraction_results. render runs JavaScript: off, shells (pages that look
        unrendered) or all, capped at renderMaxPages. Answers 'crawl this site this
        way'. Free."""
        return self.call("set_crawl_settings", _present({"clientId": client_id, "stripParams": strip_params, "extractions": extractions, "render": render, "renderMaxPages": render_max_pages, "mode": mode, "listUrls": list_urls, "includePatterns": include_patterns, "excludePatterns": exclude_patterns, "userAgent": user_agent, "requestsPerSecond": requests_per_second, "concurrency": concurrency, "maxDepth": max_depth, "maxPages": max_pages}))

    def set_keyword_notes(self, *, list_id: str, notes: List[Dict[str, Any]]) -> Any:
        """Note why keywords are on a list. Sets notes on keywords in a list — why each is
        there, which page it belongs to, what was decided — by keywordId from
        get_keyword_list. An empty note clears it; ids not on the list are ignored and
        changed says how many were set. Answers 'note that this one is for the implants
        page'. Free."""
        return self.call("set_keyword_notes", _present({"listId": list_id, "notes": notes}))

    def set_keyword_owners(self, *, client_id: str, owners: List[Dict[str, Any]], source: Optional[Literal["manual", "search_console"]] = None, dry_run: Optional[bool] = None) -> Any:
        """Say which page owns a keyword. Registers the page that owns each keyword (or
        cluster: the keyword plus its cluster members) for the client, replacing an
        earlier claim on the same keyword. build_content_brief and draft_article then
        warn when a piece would compete with the owner, and get_cannibalization says
        which page should win. Accept propose_keyword_owners' proposals with source
        search_console. dryRun: true saves nothing and lists wouldSet, each claim as it
        would be saved with the claim it would replace. Answers 'make /pricing the page
        for "crm pricing"'. Free."""
        return self.call("set_keyword_owners", _present({"clientId": client_id, "owners": owners, "source": source, "dryRun": dry_run}))

    def set_link_prospect_status(self, *, client_id: str, prospect_id: str, status: Literal["identified", "contacted", "replied", "won", "rejected"], link_url: Optional[str] = None, contact_email: Optional[str] = None) -> Any:
        """Move a link prospect to another stage. Moves one prospect on the client's
        outreach list to identified, contacted, replied, won or rejected, and saves its
        contact email. For won, give linkUrl — the page the link sits on (a page
        prospect defaults to its own page): a link check is queued to confirm the link
        is live, and the weekly link check keeps verifying it (list_link_prospects shows
        the result). Take the id from list_link_prospects. Answers 'we heard back from
        this site' and 'we got the link'. Free."""
        return self.call("set_link_prospect_status", _present({"clientId": client_id, "prospectId": prospect_id, "status": status, "linkUrl": link_url, "contactEmail": contact_email}))

    def set_path_owners(self, *, client_id: str, owners: Optional[List[Dict[str, Any]]] = None, mode: Optional[Literal["replace", "merge"]] = None, remove: Optional[List[str]] = None, dry_run: Optional[bool] = None) -> Any:
        """Say who owns which part of the site. For a site built on several platforms,
        names the owner (and a contact) of each path prefix: /docs, /blog and /community
        on one vendor, the shop on another. mode replace (the default) makes owners the
        client's whole list, and an empty list clears it; mode merge adds or updates the
        prefixes given, drops those in remove, and keeps every other. The answer lists
        the resulting owners and the changes: added, updated (with what it was), removed
        and kept. dryRun: true saves nothing and answers the same, to check a change
        first. A URL belongs to the longest prefix it falls under, on segment boundaries
        (/docs covers /docs/x, not /docsearch); / is the catch-all. Then
        get_audit_summary and list_issue_pages split issues by owner,
        create_tasks_from_audit puts the owner on each task, and the digest groups its
        fixes by owner. Answers 'the docs team owns /docs, send those fixes to them'.
        Free."""
        return self.call("set_path_owners", _present({"clientId": client_id, "owners": owners, "mode": mode, "remove": remove, "dryRun": dry_run}))

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

    def simulate_serp_snippet(self, *, client_id: Optional[str] = None, url: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None) -> Any:
        """How a result will look. Shows a page's title and meta description as Google's
        results would, measured in pixels rather than characters: what is shown and
        where it is cut with an ellipsis on desktop and on mobile, the breadcrumb URL,
        and warnings (cut, too short to survive Google's rewriting, missing — with what
        Google falls back to). Give url to read the live page, and/or title and
        description to try new wording (given text overrides the page's). Widths are
        approximations of Google's layout. Answers 'will this title be truncated' and
        'what will this look like in Google'. Free."""
        return self.call("simulate_serp_snippet", _present({"clientId": client_id, "url": url, "title": title, "description": description}))

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

    def submit_baidu_urls(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Push pages to Baidu. Pushes addresses on the client's own site to Baidu through
        Ziyuan's link submission, the only API Baidu offers a site owner. Answers 'tell
        Baidu about these pages'. Returns how many Baidu accepted and how many more it
        will take today — Baidu reports its allowance only in reply to a push. Refuses
        addresses not on the client's registered site, and refuses entirely when no
        Baidu token has been saved. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_baidu_urls", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def submit_bing_sitemap(self, *, client_id: str, sitemap_url: str) -> Any:
        """Submit a sitemap to Bing. Submits a sitemap or feed (XML sitemap, RSS 2.0, Atom
        or a text list) on the client's site to Bing Webmaster Tools. Answers 'tell Bing
        about this sitemap'. list_sitemaps then shows it with Bing's reading. Refuses
        addresses not on the client's site."""
        return self.call("submit_bing_sitemap", _present({"clientId": client_id, "sitemapUrl": sitemap_url}))

    def submit_bing_urls(self, *, client_id: str, urls: List[str], dry_run: Optional[bool] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Submit pages to Bing. Submits addresses on the client's site to Bing through
        Webmaster Tools' URL submission (SubmitUrlBatch), after reading the site's daily
        quota: addresses beyond what is left today are returned as not sent rather than
        refused by Bing one by one. Answers 'get Bing to index these pages now'. Only
        addresses on the client's own site are sent. submit_indexnow reaches Bing too,
        without the quota, once the client's IndexNow key is published. dryRun: true
        reads the quota but sends nothing, returning wouldSubmit, refused, and the
        quote. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_bing_urls", _present({"clientId": client_id, "urls": urls, "dryRun": dry_run, "maxCostMicros": max_cost_micros}))

    def submit_indexnow(self, *, client_id: str, urls: List[str], dry_run: Optional[bool] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Tell search engines a page changed. Submits changed addresses to IndexNow, which
        Bing, Yandex, Seznam and Naver share. Google does not take part. Only accepts
        addresses on a site the agency manages — anything else is refused and named.
        Answers 'we have just republished these pages, tell the engines'. Refuses
        entirely until the client's key file has been published and checked. dryRun:
        true sends nothing and returns wouldSubmit (empty when blocked says the real
        call would not send), refused, and the quote. Can spend: pass max_cost_micros to
        cap it."""
        return self.call("submit_indexnow", _present({"clientId": client_id, "urls": urls, "dryRun": dry_run, "maxCostMicros": max_cost_micros}))

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

    def submit_urls(self, *, client_id: str, urls: List[str], dry_run: Optional[bool] = None, max_cost_micros: Optional[int] = None) -> Any:
        """Submit URLs for crawling. Adds addresses to the crawl frontier for a client.
        Only accepts addresses on a site the agency manages — anything else is refused
        and named. dryRun: true adds nothing and returns wouldSubmit (the addresses as
        they would be queued), refused, and the quote. Answers 'crawl these pages I
        found'. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_urls", _present({"clientId": client_id, "urls": urls, "dryRun": dry_run, "maxCostMicros": max_cost_micros}))

    def submit_yandex_recrawl(self, *, client_id: str, urls: List[str], max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Ask Yandex to recrawl pages. Asks Yandex Webmaster to recrawl pages of the
        client's verified Yandex host, one task per page. Answers 'get Yandex to look at
        these pages again'. Returns the task id Yandex gave each queued page;
        get_yandex_performance shows the queue and the day's remaining quota. Refuses
        addresses not on the verified host (Yandex treats www and the bare domain as
        different hosts). The first quota refusal stops the rest, which come back as not
        sent. Can spend: pass max_cost_micros to cap it."""
        return self.call("submit_yandex_recrawl", _present({"clientId": client_id, "urls": urls, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def suggest_ai_prompts(self, *, client_id: str, topic: Optional[str] = None, count: Optional[int] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Suggest questions to track. Drafts questions worth tracking, grouped by topic,
        from the client brief, its brands and what is already tracked — phrased as a
        buyer would ask an assistant, never naming a tracked brand, never repeating a
        tracked question. Optionally around one topic. Nothing is saved: show them, then
        save the chosen ones with save_ai_visibility_setup. For questions people
        actually search, use keyword_explorer with mode questions. Answers 'what should
        we be tracking'. A metered Claude call. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("suggest_ai_prompts", _present({"clientId": client_id, "topic": topic, "count": count, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def suggest_ai_visibility_setup(self, *, client_id: str, seed_keywords: Optional[List[str]] = None, max_seeds: Optional[int] = None, prompts_per_seed: Optional[int] = None, max_competitors: Optional[int] = None, platform: Optional[Literal["google", "chat_gpt"]] = None, apply: Optional[bool] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Set up AI visibility from the client's own data. Drafts a client's AI visibility
        setup: its own brand (from the client's name, site and brand terms), competitors
        (from the brief and rank tracker, then DataForSEO's organic competitors to fill
        up to maxCompetitors), and starter questions grouped by topic — real questions
        people ask AI assistants, from DataForSEO's AI answer index, around the seed
        keywords (given, or the tracked keywords with the most AI search volume), each
        with its AI search volume and fan-out searches, branded or neutral. Nothing is
        saved unless apply is true, which adds them all (topics included) as
        save_ai_visibility_setup would, skipping anything already tracked. Answers 'set
        up AI tracking for this client'. A paid lookup on the client's account unless
        anyone asked the same thing recently (served says which); quote it with
        estimate_cost. (up to one competitors read, one AI volume read and one question
        read per seed) Can spend: pass max_cost_micros to cap it."""
        return self.call("suggest_ai_visibility_setup", _present({"clientId": client_id, "seedKeywords": seed_keywords, "maxSeeds": max_seeds, "promptsPerSeed": prompts_per_seed, "maxCompetitors": max_competitors, "platform": platform, "apply": apply, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def suggest_internal_links(self, *, client_id: str, crawl_id: Optional[str] = None, target_url: Optional[str] = None, phrases: Optional[List[str]] = None, limit: Optional[int] = None, format_: Optional[Literal["suggestions", "patch"]] = None, sources: Optional[List[Dict[str, Any]]] = None) -> Any:
        """Suggest internal links. Pages that already mention a topic in their text but do
        not link to the page about it, with the exact sentence and the words to use as
        the anchor, strongest linking pages first. Give targetUrl (and phrases, default:
        its title and H1 and the queries it ranks for); without a target, it picks the
        client's pages in striking distance in Search Console (positions 4–20) — where
        an internal link moves rankings most. format 'patch' also returns, per page to
        edit, a unified diff of its HTML or Markdown source (from sources, else the page
        as served) with the links inserted, and for every link the CMS-ready edit: the
        words to link, the target and the sentence with the link in it. Answers 'where
        should we add internal links' and 'give me the edits to make'. Free."""
        return self.call("suggest_internal_links", _present({"clientId": client_id, "crawlId": crawl_id, "targetUrl": target_url, "phrases": phrases, "limit": limit, "format": format_, "sources": sources}))

    def suggest_meta_tags(self, *, client_id: str, crawl_id: Optional[str] = None, urls: Optional[List[str]] = None, problems: Optional[List[Literal["missing", "duplicate", "too_long", "too_short"]]] = None, limit: Optional[int] = None, format_: Optional[Literal["rows", "csv"]] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Titles and descriptions for a whole crawl. Finds the crawled pages whose title
        or meta description is missing, duplicated, too long or too short (measured in
        pixels as Google draws them: a 600px title, a 920px description — not
        characters), and writes a new title and description for each, keeping the Search
        Console queries the page already earns clicks for. Every suggestion is
        pixel-checked again. Returns rows, and with format csv a spreadsheet of url,
        problems, current and suggested values and their widths. Answers 'fix the titles
        across the site'. Reads the latest complete crawl unless crawlId is given; urls
        narrows it. A paid Claude call per 25 pages. Can spend: pass max_cost_micros to
        cap it."""
        return self.call("suggest_meta_tags", _present({"clientId": client_id, "crawlId": crawl_id, "urls": urls, "problems": problems, "limit": limit, "format": format_, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def sync_local_reviews(self, *, client_id: str, location_id: str, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """Collect a location's Google reviews. Collects the location's latest Google
        reviews (up to 50) from the vendor. Paid: quote it with estimate_cost first.
        Runs in the background and takes a few minutes; read the analysis with
        get_local_visibility afterwards. A second request within the hour lands on the
        collection already running rather than paying twice. With maxCostMicros, it is
        refused before it starts when its estimate is over the limit. Answers 'pull in
        our latest reviews'. Can spend: pass max_cost_micros to cap it."""
        return self.call("sync_local_reviews", _present({"clientId": client_id, "locationId": location_id, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def sync_outreach(self, *, client_id: str) -> Any:
        """Check outreach threads for replies, and send due follow-ups. Does now what the
        hourly sweep does for this client: reads every live outreach thread for a reply
        (moving a prospect who answered to replied and calling off its follow-ups), then
        sends the follow-ups that are due. Answers 'did anyone reply to our outreach'.
        No vendor charge; it sends due follow-ups, so it needs client:manage."""
        return self.call("sync_outreach", _present({"clientId": client_id}))

    def sync_search_console(self, *, client_id: str) -> Any:
        """Collect Search Console data now. Collects the latest days from Search Console
        now instead of waiting for the nightly sync — and the sixteen-month history too
        if it is still owed. Runs in the background for a minute or two; read the data
        with the Search Console tools afterwards. Returns the previous sync's time and
        note: a note saying Google reported no search data means the property had no
        impressions on those days (a new or barely visible site), not a broken
        connection. Answers 'pull our Search Console data now'. Free."""
        return self.call("sync_search_console", _present({"clientId": client_id}))

    def sync_task_statuses(self, *, client_id: str) -> Any:
        """Sync task status with the tracker now. Reads every mirrored issue's state now
        and brings each pair into step: an issue moved in the tracker moves its task, a
        task moved here moves its issue (GitHub has no in-progress, so an open issue
        stays open). The hourly sync does this on its own. Answers 'did they close the
        Jira tickets'. Free."""
        return self.call("sync_task_statuses", _present({"clientId": client_id}))

    def tag_keywords(self, *, client_id: str, tracker_id: str, keyword_ids: List[str], tags: List[str], remove: Optional[bool] = None) -> Any:
        """Tag tracked keywords. Puts tags on a tracker's keywords, or takes them off with
        remove: true. Answers 'label these as our brand terms'. Tags are
        case-insensitive labels such as 'brand' or 'money terms' that the tracker view
        filters by. Keywords the tracker does not track are returned in notTracked
        rather than tagged."""
        return self.call("tag_keywords", _present({"clientId": client_id, "trackerId": tracker_id, "keywordIds": keyword_ids, "tags": tags, "remove": remove}))

    def tag_list_keywords(self, *, list_id: str, keyword_ids: Optional[List[str]], tags: List[str], remove: Optional[bool] = None) -> Any:
        """Tag keywords on a list. Puts tags on keywords in a list, or takes them off with
        remove: true — by keywordId from query_keyword_list, or keywordIds: 'all' for
        every keyword on the list. Answers 'tag these as pillar' and 'take q3 off the
        whole list'. Tags are case-insensitive labels up to 40 characters; changed
        counts the keywords that gained or lost one. For a tracker's keywords use
        tag_keywords. Free."""
        return self.call("tag_list_keywords", _present({"listId": list_id, "keywordIds": keyword_ids, "tags": tags, "remove": remove}))

    def test_robots(self, *, client_id: str, urls: List[str], bots: Optional[List[str]] = None) -> Any:
        """Can this bot fetch this page. Reads the client's live robots.txt and says, for
        each address and each crawler, whether it may fetch it and which line decides —
        for every search engine and AI crawler by default (Googlebot, Bingbot, Applebot,
        DuckDuckBot, YandexBot, Baiduspider, GPTBot, OAI-SearchBot, ChatGPT-User,
        ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User,
        Google-Extended, Applebot-Extended, Meta-ExternalAgent, Bytespider, CCBot,
        Amazonbot, DuckAssistBot, MistralAI-User, AhrefsBot, SemrushBot), or the tokens
        in bots. Same parser the crawler obeys. Answers 'can GPTBot read our pricing
        page', 'are we blocking Google-Extended' and 'which rule blocks Googlebot here'.
        Free."""
        return self.call("test_robots", _present({"clientId": client_id, "urls": urls, "bots": bots}))

    def unaccept_issue(self, *, client_id: str, ids: List[str]) -> Any:
        """Stop accepting an issue. Removes acceptances by id (from list_accepted_issues),
        so their findings count again in the scorecard, audit summary, digest, tasks and
        alerts. Unknown ids are ignored. Answers 'start flagging those pages again'.
        Free."""
        return self.call("unaccept_issue", _present({"clientId": client_id, "ids": ids}))

    def update_alert_rule(self, *, client_id: str, rule_id: str, threshold: Optional[int] = None, cooldown_hours: Optional[int] = None, webhook_url: Optional[str] = None, channel: Optional[Literal["slack", "webhook", "email", "telegram"]] = None, email_recipients: Optional[List[str]] = None, telegram_chat_id: Optional[str] = None, paused: Optional[bool] = None, paid_source: Optional[bool] = None) -> Any:
        """Update an alert rule. Changes a rule's threshold, cooldown or delivery (channel,
        webhookUrl — null removes it — emailRecipients, telegramChatId), or pauses and
        resumes it, or turns its paidSource on or off. Answers 'this alert is too
        noisy', 'send this to email instead' or 'mute this for now'. Pausing keeps the
        rule's history. paidSource (competitor-new-keywords and web-mentions only; off
        by default; needs spend permission) also buys the signal from DataForSEO on
        every sweep: for competitor-new-keywords, Labs ranked keywords each tracker
        competitor (up to 5) newly ranks for at the tracker's market, not only tracked
        keywords; for web-mentions, pages DataForSEO's content index first saw naming
        the brand, off the client's own domains. The sweep is hourly but a purchase is
        reused from the archive while fresh, so it buys at most once a week per
        competitor (once a day for mentions); it is capped by the client's monthly
        budget, and a failed or over-budget read falls back to the free signal. Quote it
        first with estimate_cost."""
        return self.call("update_alert_rule", _present({"clientId": client_id, "ruleId": rule_id, "threshold": threshold, "cooldownHours": cooldown_hours, "webhookUrl": webhook_url, "channel": channel, "emailRecipients": email_recipients, "telegramChatId": telegram_chat_id, "paused": paused, "paidSource": paid_source}))

    def update_business_profile(self, *, client_id: str, changes: Dict[str, Any], location_id: Optional[str] = None, dry_run: Optional[bool] = None) -> Any:
        """Change a Google Business Profile listing. Changes the client's own Google
        Business Profile listing through its connected Business Profile (the connection
        review replies are posted with): regularHours (the whole week, 24-hour HH:MM,
        closeDay past midnight), specialHours (holidays and one-off dates, closed or
        open–close; needs regular hours on the listing), description (up to 750
        characters), phone (primary and up to two additional), website, categories
        (Google ids such as gcid:dentist; primary and up to nine additional) and simple
        yes/no attributes by Google id. Only the fields given are changed
        (locations.patch with an updateMask; attributes through updateAttributes); phone
        and category lists Google replaces whole keep the half not given from the
        listing. dryRun: true changes nothing and returns the exact patch and
        updateMask, the listing's fields before and after, and Google's own check of the
        change (validateOnly) — show it to the person first. Refused with missing_scope
        when the connection was not granted permission to manage the listing, and
        not_connected when the location has none; next says how to connect it. Google
        may hold a change for review before it shows. Answers 'update our opening hours'
        and 'change the business description'. Free."""
        return self.call("update_business_profile", _present({"clientId": client_id, "locationId": location_id, "changes": changes, "dryRun": dry_run}))

    def update_client(self, *, client_id: str, name: Optional[str] = None, monthly_budget_usd: Optional[float] = None) -> Any:
        """Update a client. Renames a client or changes its monthly vendor spend cap (null
        removes the cap). Answers 'rename this client' or 'cap this client's spend'. The
        cap is enforced on every paid lookup from then on."""
        return self.call("update_client", _present({"clientId": client_id, "name": name, "monthlyBudgetUsd": monthly_budget_usd}))

    def update_client_brief(self, *, client_id: str, overview: Optional[str] = None, goal: Optional[str] = None, positioning: Optional[str] = None, audience: Optional[str] = None, voice: Optional[str] = None, add: Optional[List[Dict[str, Any]]] = None, update: Optional[List[Dict[str, Any]]] = None, remove: Optional[List[str]] = None, brand_terms: Optional[List[str]] = None) -> Any:
        """Update the client brief. Changes the client brief that every teammate and agent
        reads. Answers 'remember this about the client'. Set fields (overview, goal,
        positioning, audience, voice; null or empty clears one, fields left out are
        untouched); add entries (kind competitor, key_page, section or research, each
        with a title and optional body and url); edit entries by id; remove entries by
        id (unknown ids are ignored); replace the brand terms (brandTerms) that split
        branded from non-branded search. Applied in that order, so removing an old
        competitor and adding its replacement in one call works. Record a research entry
        when you finish a piece of work whose conclusions the next one should start
        from; the 50 newest research notes are kept. Returns the brief as it now stands.
        Free."""
        return self.call("update_client_brief", _present({"clientId": client_id, "overview": overview, "goal": goal, "positioning": positioning, "audience": audience, "voice": voice, "add": add, "update": update, "remove": remove, "brandTerms": brand_terms}))

    def update_content_plan_item(self, *, client_id: str, id_: str, month: Optional[str] = None, publish_on: Optional[str] = None, status: Optional[Literal["planned", "briefed", "drafting", "published", "dropped"]] = None, target_url: Optional[str] = None, notes: Optional[str] = None, keyword: Optional[str] = None) -> Any:
        """Change a planned piece. Moves a planned piece to another month or date, changes
        its status (planned, briefed, drafting, published, dropped), target URL, keyword
        or notes. Answers 'mark that article published' and 'push this to May'. Free."""
        return self.call("update_content_plan_item", _present({"clientId": client_id, "id": id_, "month": month, "publishOn": publish_on, "status": status, "targetUrl": target_url, "notes": notes, "keyword": keyword}))

    def update_data_sync(self, *, client_id: str, sync_id: str, name: Optional[str] = None, query: Optional[Dict[str, Any]] = None, mode: Optional[Literal["append", "replace"]] = None, window_days: Optional[int] = None, cadence: Optional[Literal["daily", "weekly", "monthly"]] = None, run_hour: Optional[int] = None, paused: Optional[bool] = None) -> Any:
        """Change a data sync. Changes a sync's name, query, mode, window, cadence or hour,
        or pauses or resumes it; only what is passed changes. Answers 'make the sheet
        weekly' and 'pause the BigQuery export'. Free."""
        return self.call("update_data_sync", _present({"clientId": client_id, "syncId": sync_id, "name": name, "query": query, "mode": mode, "windowDays": window_days, "cadence": cadence, "runHour": run_hour, "paused": paused}))

    def update_lead_widget(self, *, widget_id: str, name: Optional[str] = None, heading: Optional[str] = None, accent_color: Optional[str] = None, allowed_origins: Optional[List[str]] = None, notify_emails: Optional[List[str]] = None, enabled: Optional[bool] = None) -> Any:
        """Change a lead-gen widget. Renames a widget, changes its heading, colour, allowed
        sites or who is notified, or switches it off and on (enabled). A switched-off
        form stops taking requests at once; its leads are kept. Answers 'turn off the
        form on our old site'. Free."""
        return self.call("update_lead_widget", _present({"widgetId": widget_id, "name": name, "heading": heading, "accentColor": accent_color, "allowedOrigins": allowed_origins, "notifyEmails": notify_emails, "enabled": enabled}))

    def update_portfolio(self, *, portfolio_id: str, name: Optional[str] = None, description: Optional[str] = None, add: Optional[List[Dict[str, Any]]] = None, remove: Optional[List[Dict[str, Any]]] = None) -> Any:
        """Change a portfolio. Renames or re-describes a portfolio, and adds or removes
        members — a whole client, or one site with its client. Renaming needs access to
        every client in it. Adding a member already there is a no-op. Answers 'add this
        client to the retail portfolio'."""
        return self.call("update_portfolio", _present({"portfolioId": portfolio_id, "name": name, "description": description, "add": add, "remove": remove}))

    def update_rank_tracker(self, *, client_id: str, tracker_id: str, name: Optional[str] = None, device: Optional[Literal["desktop", "mobile", "both"]] = None, frequency: Optional[Literal["daily", "weekly", "monthly", "manual"]] = None, run_hour: Optional[int] = None, run_day: Optional[int] = None, depth: Optional[int] = None, match: Optional[Literal["domain", "subdomains", "prefix"]] = None, url_prefix: Optional[str] = None) -> Any:
        """Update a rank tracker. Renames a tracker or changes its device (desktop, mobile
        or both), cadence (daily, weekly, monthly, or manual — only when
        refresh_rankings asks), the hour and day it runs, how deep it reads (10–200
        results), or what counts as the client (the exact host, every subdomain, or only
        a folder or page via urlPrefix). Answers 'check these weekly instead', 'track
        only our /blog/ pages'. Weekly costs a seventh as much, monthly a thirtieth."""
        return self.call("update_rank_tracker", _present({"clientId": client_id, "trackerId": tracker_id, "name": name, "device": device, "frequency": frequency, "runHour": run_hour, "runDay": run_day, "depth": depth, "match": match, "urlPrefix": url_prefix}))

    def update_report_schedule(self, *, client_id: str, schedule_id: str, cadence: Optional[Literal["monthly", "weekly"]] = None, recipients: Optional[List[str]] = None, paused: Optional[bool] = None) -> Any:
        """Change a report schedule. Changes a schedule's cadence or recipients, or pauses
        or resumes it. Answers 'add the new marketing lead to the monthly report' and
        'stop the weekly email while the client is away'. Recipients, when given,
        replace the whole list. A paused schedule sends nothing until resumed."""
        return self.call("update_report_schedule", _present({"clientId": client_id, "scheduleId": schedule_id, "cadence": cadence, "recipients": recipients, "paused": paused}))

    def update_task(self, *, client_id: str, task_id: str, title: Optional[str] = None, notes: Optional[str] = None, status: Optional[Literal["todo", "in_progress", "done", "wont_do"]] = None, assignee_user_id: Optional[str] = None, due_date: Optional[str] = None, link: Optional[Dict[str, Any]] = None) -> Any:
        """Change a task. Changes a task's title, notes, status, assignee, due date or
        link; only what is passed changes, and null clears. Moving to done or wont_do
        records when; moving back to todo clears it. Answers 'mark the title fixes done'
        and 'give this to Sam for next week'."""
        return self.call("update_task", _present({"clientId": client_id, "taskId": task_id, "title": title, "notes": notes, "status": status, "assigneeUserId": assignee_user_id, "dueDate": due_date, "link": link}))

    def validate_product_schema(self, *, client_id: str, urls: Optional[List[str]] = None, limit: Optional[int] = None, eu: Optional[bool] = None, render: Optional[Literal["off", "auto"]] = None) -> Any:
        """Check Product and Offer structured data. Reads product pages and checks their
        Product and Offer JSON-LD against what Google's merchant listings need — errors:
        name, image, offers as Offer (not AggregateOffer) with a price above 0 and an
        ISO 4217 priceCurrency (or a priceSpecification), a valid availability;
        warnings: brand (its name not empty or N/A), a GTIN or MPN or SKU, description,
        offers.url, itemCondition, priceValidUntil when it has passed, validFrom without
        an end date, shipping details with shippingDestination and deliveryTime, a
        return policy with applicableCountry and returnPolicyCategory, a rating with
        ratingValue and reviewCount, hasAdultConsideration values, a ProductGroup's
        productGroupID, variesBy and hasVariant, and with eu: true the energy efficiency
        class; notes: returnPolicyCountry, member programs, variants — says whether each
        page is eligible, and gives a completenessScore (required fields 50,
        aggregateRating 65, an identifier 75, shippingDetails 85, a return policy 90,
        three or more reviews 100). With no urls, the latest crawl's pages that carry
        Product markup (up to limit). render 'auto' renders a page in a browser when its
        HTML carries no Product markup, for stores that inject their JSON-LD with
        JavaScript. Answers 'is our product schema right' and 'why don't our products
        show prices in Google'. Free."""
        return self.call("validate_product_schema", _present({"clientId": client_id, "urls": urls, "limit": limit, "eu": eu, "render": render}))

    def validate_sitemap(self, *, client_id: str, crawl_id: Optional[str] = None, check_files: Optional[bool] = None) -> Any:
        """Is the sitemap telling the truth. Checks the sitemaps a crawl read against the
        pages it found: entries that do not answer 200, are noindexed or are
        canonicalised elsewhere; indexable pages no sitemap lists (the sitemap's
        coverage of the crawl) and listed pages the crawl never reached (the crawl's
        coverage of the sitemap); lastmod accuracy against the previous crawl (content
        changed but lastmod did not, lastmod moved but nothing changed, dates in the
        future, every entry stamped with the build date); image and video sitemap
        coverage; and the entries added, removed and re-dated since the previous crawl.
        With checkFiles (default on) it also reads each sitemap file live, up to 20 —
        robots.txt's Sitemap: lines, the files the crawl read and what an index names —
        and judges each on its own: over 50,000 URLs or 50 MB uncompressed (critical),
        XML errors with their line number, not declared in robots.txt, http:// entries,
        <priority>/<changefreq> (ignored by Google), over 1,000 image:image per URL and
        the deprecated image tags, video entries missing thumbnail_loc, title,
        description or a content/player address, and news sitemaps over 1,000 entries,
        older than two days or missing publication name, language, date or title.
        Answers 'is our sitemap clean', 'does Google trust our lastmod' and 'which pages
        are missing from the sitemap'. Free."""
        return self.call("validate_sitemap", _present({"clientId": client_id, "crawlId": crawl_id, "checkFiles": check_files}))

    def validate_structured_data(self, *, client_id: str, url: Optional[str] = None, crawl_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
        """Structured data against Google's requirements. Checks JSON-LD against what
        Google's search gallery requires and recommends for each rich result type —
        Article, Breadcrumb, Course list (Course + ItemList), Carousel (ItemList),
        Dataset, Discussion forum, Event, Image metadata, Job posting, Local business,
        Movie, Organization, Product (snippets and merchant listings), Profile page,
        Q&A, Recipe, Review and rating, Software app, Vacation rental, Video, Site name
        — plus FAQ (retired for every site on 7 May 2026), HowTo, the 2025–2026
        retirements (special announcement, fact check, vehicle listing, estimated
        salary, practice problem), Service and SoftwareSourceCode, which earn no rich
        result any more (or never did). Values Google cannot read (non-ISO dates and
        durations, prices with currency signs, relative URLs that are not URLs) are
        errors. Give url to read one of the client's pages live, or a crawlId (default
        latest) for the whole site by type: pages, how many are valid, and the
        properties most often missing. Answers 'is our product markup eligible for rich
        results' and 'what structured data is broken'. Free."""
        return self.call("validate_structured_data", _present({"clientId": client_id, "url": url, "crawlId": crawl_id, "limit": limit}))

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

    def wait_for_job(self, *, client_id: str, job_id: str, timeout_seconds: Optional[int] = None) -> Any:
        """Wait for a slow job. get_job that waits: holds the call open until the job
        finishes or timeoutSeconds pass (at most 60), then answers with its status, so
        an agent makes one call instead of polling. Call again while it says running.
        Answers 'wait for the crawl'. Free."""
        return self.call("wait_for_job", _present({"clientId": client_id, "jobId": job_id, "timeoutSeconds": timeout_seconds}))

    def whoami(self) -> Any:
        """Who am I connected as. Says who this connection is: the agency, whether it is an
        API key or a person, the role, every permission that role holds, and the clients
        it can reach. Answers 'what can this key do'. Call it first when unsure whether
        a task is allowed. Free."""
        return self.call("whoami", {})

    def youtube_keyword_research(self, *, client_id: str, seed: str, measure: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """YouTube search phrases around a topic. What people type into YouTube around a
        seed, in YouTube's own order of popularity (its suggestions; YouTube publishes
        no search volume, so none is given), and for the first measure phrases how
        crowded the results are: the top videos' median views, how many are from the
        last year, how many channels share them and how many are Shorts. Answers 'what
        should our next video target' and 'which YouTube phrases are winnable'.
        Suggestions are free; each phrase measured is one YouTube results page: A paid
        lookup on the client's account unless anyone read the same thing today (spend
        says which); quote it with estimate_cost. Can spend: pass max_cost_micros to cap
        it."""
        return self.call("youtube_keyword_research", _present({"clientId": client_id, "seed": seed, "measure": measure, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))

    def youtube_video_brief(self, *, client_id: str, keyword: str, videos: Optional[int] = None, location_code: Optional[int] = None, language_code: Optional[str] = None, max_cost_micros: Optional[int] = None, dry_run: Optional[bool] = None) -> Any:
        """A title, description and chapter brief from the top videos. Reads the videos
        ranking on YouTube for a phrase (the results page, then each video's details)
        and writes the brief for a video to beat them: how their titles are built
        (length, the phrase first, numbers, brackets, the year) with examples, how long
        their descriptions run and how many use chapters and hashtags, the chapter
        labels they share in their usual order, the tags they use most, and how long the
        videos are. Answers 'how should we title and structure this video'. One results
        page plus one read per video: A paid lookup on the client's account unless
        anyone read the same thing today (spend says which); quote it with
        estimate_cost. Can spend: pass max_cost_micros to cap it."""
        return self.call("youtube_video_brief", _present({"clientId": client_id, "keyword": keyword, "videos": videos, "locationCode": location_code, "languageCode": language_code, "maxCostMicros": max_cost_micros, "dryRun": dry_run}))
