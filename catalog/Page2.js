import React from 'react';
import { Page, Text, View, StyleSheet, Svg, Path } from '@react-pdf/renderer';
import { colors, commonStyles } from './styles';

const styles = StyleSheet.create({
  page: {
    ...commonStyles.page,
  },
  header: {
    ...commonStyles.header,
    paddingBottom: 12,
    marginBottom: 12,
  },
  headerLeft: {
    flexDirection: 'column',
  },
  headerTitle: {
    fontSize: 24,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
    marginBottom: 4,
  },
  headerSubtitle: {
    fontSize: 9,
    color: colors.slate600,
    fontFamily: 'Helvetica-Bold',
  },
  headerRight: {
    flexDirection: 'column',
    alignItems: 'flex-end',
  },
  apBadge: {
    width: 24,
    height: 24,
    backgroundColor: colors.brandGradientStart,
    borderRadius: 4,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 4,
  },
  apText: {
    color: 'white',
    fontSize: 10,
    fontFamily: 'Helvetica-Bold',
  },
  catalogYear: {
    fontSize: 7,
    color: colors.slate400,
    fontFamily: 'Helvetica-Bold',
    textTransform: 'uppercase',
    letterSpacing: 1.5,
  },
  gridContainer: {
    flexDirection: 'row',
    gap: 12,
    flex: 1,
    marginBottom: 16,
  },
  column: {
    flex: 1,
    borderRadius: 12,
    padding: 12,
    borderWidth: 1,
  },
  columnPurple: {
    backgroundColor: colors.purple50,
    borderColor: '#E9D5FF',
  },
  columnWhite: {
    backgroundColor: '#FFFFFF',
    borderColor: colors.slate200,
  },
  columnSlate: {
    backgroundColor: colors.slate50,
    borderColor: colors.slate200,
  },
  columnHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 10,
  },
  columnMarker: {
    width: 4,
    height: 20,
    borderRadius: 2,
  },
  columnTitle: {
    fontSize: 8,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  serviceCard: {
    backgroundColor: 'white',
    borderRadius: 8,
    padding: 12,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: colors.slate200,
  },
  serviceCardPurple: {
    borderColor: '#E9D5FF',
  },
  serviceHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 6,
  },
  serviceTitle: {
    fontSize: 11,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
    flex: 1,
  },
  serviceDescription: {
    fontSize: 8,
    color: colors.slate600,
    lineHeight: 1.4,
    marginBottom: 8,
  },
  servicePricing: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    borderTopWidth: 1,
    borderTopColor: colors.slate50,
    paddingTop: 8,
  },
  servicePrice: {
    fontSize: 13,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
  },
  serviceTag: {
    fontSize: 7,
    fontFamily: 'Helvetica-Bold',
    color: colors.purple600,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  footer: {
    ...commonStyles.footer,
  },
  footerLeft: {
    flexDirection: 'row',
    gap: 24,
  },
  footerRight: {
    flexDirection: 'row',
    gap: 8,
    alignItems: 'center',
  },
  footerDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: colors.emerald500,
  },
  footerPage: {
    fontSize: 9,
    color: colors.slate500,
  },
});

const ServiceCard = ({ title, description, price, tag, isPurple }) => (
  <View style={[styles.serviceCard, isPurple && styles.serviceCardPurple]}>
    <View style={styles.serviceHeader}>
      <Text style={styles.serviceTitle}>{title}</Text>
    </View>
    <Text style={styles.serviceDescription}>{description}</Text>
    <View style={styles.servicePricing}>
      <Text style={styles.servicePrice}>{price}</Text>
      <Text style={styles.serviceTag}>{tag}</Text>
    </View>
  </View>
);

const Page2 = () => (
  <Page size="A4" orientation="landscape" style={styles.page}>
    {/* Header */}
    <View style={styles.header}>
      <View style={styles.headerLeft}>
        <Text style={styles.headerTitle}>Complete Service Catalog</Text>
        <Text style={styles.headerSubtitle}>Fixed-price diagnostics. Project-based implementations. Retainer partnerships.</Text>
      </View>
      <View style={styles.headerRight}>
        <View style={styles.apBadge}>
          <Text style={styles.apText}>AP</Text>
        </View>
        <Text style={styles.catalogYear}>Service Catalog 2026</Text>
      </View>
    </View>

    {/* Grid Container */}
    <View style={styles.gridContainer}>
      {/* Column 1: Diagnostics */}
      <View style={[styles.column, styles.columnPurple]}>
        <View style={styles.columnHeader}>
          <View style={[styles.columnMarker, { backgroundColor: colors.purple600 }]} />
          <Text style={styles.columnTitle}>Diagnostics</Text>
        </View>
        <ServiceCard
          title="Technical Health Audit"
          description="We analyze metadata, Apex code, and flows to expose the cracks before they break."
          price="€2,450"
          tag="One-Time"
          isPurple
        />
        <ServiceCard
          title="Data Quality Check"
          description="Analyze full data model for bloat, broken refs, and performance killers."
          price="From €800"
          tag="Audit"
          isPurple
        />
        <ServiceCard
          title="GDPR Compliance"
          description="Identify personal data exposure and risky access patterns."
          price="~€1,200"
          tag="Check Risk"
          isPurple
        />
      </View>

      {/* Column 2: Core Cloud */}
      <View style={[styles.column, styles.columnWhite]}>
        <View style={styles.columnHeader}>
          <View style={[styles.columnMarker, { backgroundColor: colors.slate300 }]} />
          <Text style={styles.columnTitle}>Core Cloud</Text>
        </View>
        <ServiceCard
          title="Sales Cloud Velocity"
          description="Configure Pipeline management & Lead-to-Cash workflows for speed."
          price="€5k - €15k"
          tag="Configure"
        />
        <ServiceCard
          title="Service Console"
          description="Implement Omni-Channel routing, Case Management, and SLAs."
          price="€5k - €15k"
          tag="Setup"
        />
        <ServiceCard
          title="Marketing Cloud"
          description="Architect data-driven Journeys, Automations, and engagement."
          price="Custom Quote"
          tag="Discuss"
        />
      </View>

      {/* Column 3: Engineering */}
      <View style={[styles.column, styles.columnSlate]}>
        <View style={styles.columnHeader}>
          <View style={[styles.columnMarker, { backgroundColor: colors.slate600 }]} />
          <Text style={styles.columnTitle}>Engineering</Text>
        </View>
        <ServiceCard
          title="Custom Dev"
          description="Clean, maintainable Apex, LWC, and Flows tailored to your exact use case."
          price="€100-150/hr"
          tag="Agile Dev"
        />
        <ServiceCard
          title="System Integrations"
          description="Wire Salesforce to ERP, Marketing Stack, or internal tools using robust APIs."
          price="€15k - €30k"
          tag="Integrate"
        />
        <ServiceCard
          title="Mulesoft Arch."
          description="Architect Mulesoft flows moving clean, validated data across ecosystems."
          price="€5k - €30k"
          tag="Consult"
        />
      </View>

      {/* Column 4: Stability & Scale */}
      <View style={[styles.column, styles.columnPurple]}>
        <View style={styles.columnHeader}>
          <View style={[styles.columnMarker, { backgroundColor: colors.brandGradientStart }]} />
          <Text style={styles.columnTitle}>Stability & Scale</Text>
        </View>
        <ServiceCard
          title="Managed Support"
          description="Monitor, triage, and resolve user issues and bugs within 24 hours."
          price="€3k - €8k/mo"
          tag="Retainer"
          isPurple
        />
        <ServiceCard
          title="CI/CD Pipeline"
          description="Setup version control, automated testing, and safe deployments."
          price="€10k - €20k"
          tag="DevOps"
          isPurple
        />
        <ServiceCard
          title="Technical Lead"
          description="Fractional CTO for Salesforce—architecture reviews, roadmaps, governance."
          price="€5k+/mo"
          tag="Strategy"
          isPurple
        />
      </View>
    </View>

    {/* Footer */}
    <View style={styles.footer}>
      <View style={styles.footerLeft}>
        <Text style={commonStyles.footerText}>info@apexpalantir.com</Text>
        <Text style={commonStyles.footerText}>•</Text>
        <Text style={commonStyles.footerText}>+49 173 237 518 3</Text>
      </View>
      <View style={styles.footerRight}>
        <View style={styles.footerDot} />
        <Text style={commonStyles.footerTextLight}>Remote First. Europe Wide.</Text>
        <Text style={[commonStyles.footerText, { marginLeft: 12 }]}>•</Text>
        <Text style={styles.footerPage}>Page 02</Text>
      </View>
    </View>
  </Page>
);

export default Page2;
