# SEO deployment checklist

1. Replace every `https://YOUR-DOMAIN.example` with the real published website URL.
2. Keep `index.html` at the repository root.
3. Publish with GitHub Pages.
4. In Google Search Console, verify the site and submit `/sitemap.xml`.
5. Use URL Inspection to request indexing for the home page and blog index.
6. Validate structured data with Google's Rich Results Test.
7. Create only genuine profiles/directories and avoid automated guestbook/forum link spam.
8. Ask real clients for honest reviews; never fabricate testimonials.

Google notes that structured data helps it understand content but does not guarantee a rich result, and that sitemaps help Google discover URLs.


## Homepage SEO metadata update
The homepage now uses a single consolidated meta description, stronger robots directives, Open Graph metadata, Twitter card metadata, and a theme color. Placeholder canonical/og URL values were removed rather than publishing a fake domain. Once the live domain is known, add an absolute canonical URL and matching `og:url` to `index.html`.


## Step 15 — indexing readiness
- Canonical URL now points to the published GitHub Pages homepage.
- Open Graph URL now matches the published homepage.
- robots.txt allows crawling and points to the XML sitemap.
- sitemap.xml includes the published homepage and core pages.
- In Google Search Console, add the GitHub Pages property, submit `/tyt/sitemap.xml`, then use URL Inspection to request indexing for the homepage.

## Step 16 — internal SEO
- Added canonical, Open Graph, and Twitter metadata to supporting pages.
- Added consistent internal navigation across About, Reviews, Privacy, and Terms.
- Simplified the sitemap to canonical public URLs and added last-modified dates and priorities.
- Keep page titles descriptive and avoid duplicate or fabricated review content.


## Step 19 content cluster
Added a Guides hub plus three original educational pages targeting informational searches around cryptocurrency scams, transaction tracing, and recovery scams. These pages are included in sitemap.xml and linked internally from the homepage.
