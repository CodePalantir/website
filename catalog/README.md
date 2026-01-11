# ApexPalantir Service Catalog (PDF Generation)

This directory contains two versions for generating the Service Catalog PDF:
1. **HTML Version**: Standalone HTML files for browser-based PDF export
2. **React PDF Version**: React-based programmatic PDF generation

## Structure

```
catalog/
├── page-1.html          # HTML: Cover & Value Proposition
├── page-2.html          # HTML: Complete Service Overview
├── page-3.html          # HTML: Why ApexPalantir + Next Steps
├── catalog-full.html    # HTML: All pages combined for PDF export
├── package.json         # React PDF: Dependencies
├── index.js             # React PDF: Generation script
├── App.js               # React PDF: Main document component
├── styles.js            # React PDF: Shared styles
├── Page1.js             # React PDF: Page 1 component
├── Page2.js             # React PDF: Page 2 component
├── Page3.js             # React PDF: Page 3 component
└── README.md
```

## How to Use

### HTML Version (Browser-Based)
1. Edit individual page HTML files (page-1.html, page-2.html, etc.)
2. Preview in browser (open HTML files directly)
3. When ready to export PDF:
   - Open `catalog-full.html` in Chrome/Firefox
   - File > Print > Save as PDF
   - Or use automated tools (see below)

### React PDF Version (Programmatic)
1. Install dependencies:
   ```bash
   cd catalog
   npm install
   ```
2. Generate PDF:
   ```bash
   npm run generate
   ```
3. Output: `ApexPalantir-Service-Catalog-2026.pdf` in the catalog directory
4. To customize:
   - Edit `Page1.js`, `Page2.js`, `Page3.js` for content
   - Edit `styles.js` for colors and styling

## PDF Export Options

### Option 1: Browser Print (Simple)
1. Open `catalog-full.html` in Chrome
2. Cmd+P (Mac) or Ctrl+P (Windows)
3. Destination: "Save as PDF"
4. Paper size: A4 Landscape
5. Margins: None
6. Save

### Option 2: Automated with Puppeteer (Advanced)
```bash
npm install -g puppeteer
node catalog/export-pdf.js
```

### Option 3: Online Tools
- Upload `catalog-full.html` to services like:
  - WeasyPrint
  - Prince XML
  - PDFShift

## Excluded from Jekyll Build

The `catalog/` directory is excluded from Jekyll site generation via `_config.yml`.
These files are standalone and won't appear on the live website.

## Notes

- All styles are inline or in `assets/css/catalog.css` for portability
- Images should use relative paths: `assets/images/filename.png`
- A4 Landscape: 297mm x 210mm (11.69" x 8.27")
- Print-optimized CSS uses `@media print` queries
