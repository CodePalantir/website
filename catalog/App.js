import React from 'react';
import { Document } from '@react-pdf/renderer';
import Page1 from './Page1';
import Page2 from './Page2';
import Page3 from './Page3';

const ApexPalantirCatalog = () => (
  <Document
    title="ApexPalantir Service Catalog 2026"
    author="ApexPalantir"
    subject="Complete service catalog for Salesforce engineering and consulting"
    creator="ApexPalantir"
  >
    <Page1 />
    <Page2 />
    <Page3 />
  </Document>
);

export default ApexPalantirCatalog;
