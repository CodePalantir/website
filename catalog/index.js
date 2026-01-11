import React from 'react';
import ReactPDF from '@react-pdf/renderer';
import ApexPalantirCatalog from './App';
import fs from 'fs';
import path from 'path';

const generatePDF = async () => {
  try {
    console.log('Generating ApexPalantir Service Catalog PDF...');

    const outputPath = path.join(__dirname, 'ApexPalantir-Service-Catalog-2026.pdf');

    // Render the PDF to a file
    await ReactPDF.render(<ApexPalantirCatalog />, outputPath);

    console.log(`✓ PDF generated successfully: ${outputPath}`);
    console.log('File size:', (fs.statSync(outputPath).size / 1024).toFixed(2), 'KB');
  } catch (error) {
    console.error('Error generating PDF:', error);
    process.exit(1);
  }
};

generatePDF();
