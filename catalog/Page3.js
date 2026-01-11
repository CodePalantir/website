import React from 'react';
import { Page, Text, View, StyleSheet, Svg, Path, Line, Circle, Rect, Defs, LinearGradient, Stop } from '@react-pdf/renderer';
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
  heroSection: {
    height: '60%',
    paddingHorizontal: 64,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  heroLeft: {
    width: '60%',
    paddingRight: 48,
  },
  heroTitle: {
    fontSize: 48,
    lineHeight: 1.1,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
    marginBottom: 24,
  },
  heroPurple: {
    color: colors.brandGradientStart,
  },
  heroSubtitle: {
    fontSize: 18,
    color: colors.slate600,
    lineHeight: 1.6,
  },
  decorativeLine: {
    marginTop: 32,
  },
  heroRight: {
    width: '40%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  chartCard: {
    backgroundColor: colors.slate50,
    borderRadius: 24,
    padding: 32,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    width: 380,
  },
  chartTitle: {
    fontSize: 16,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
    marginBottom: 24,
  },
  chartBottom: {
    marginTop: 16,
    alignItems: 'center',
  },
  chartLabel: {
    fontSize: 11,
    color: colors.slate600,
    marginBottom: 4,
  },
  chartMetric: {
    fontSize: 20,
    fontFamily: 'Helvetica-Bold',
    color: colors.brandGradientStart,
  },
  ctaSection: {
    height: '25%',
    paddingHorizontal: 64,
    paddingBottom: 32,
  },
  ctaGrid: {
    flexDirection: 'row',
    gap: 32,
    height: '100%',
  },
  ctaCard: {
    flex: 1,
    backgroundColor: colors.slate50,
    borderRadius: 16,
    padding: 24,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    justifyContent: 'center',
  },
  ctaCardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 12,
  },
  ctaIconBox: {
    padding: 8,
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
  },
  ctaCardTitle: {
    fontFamily: 'Helvetica-Bold',
    fontSize: 16,
    color: colors.slate900,
  },
  ctaCardText: {
    fontSize: 11,
    color: colors.slate600,
    lineHeight: 1.5,
    marginBottom: 12,
  },
  ctaPrice: {
    fontSize: 24,
    fontFamily: 'Helvetica-Bold',
    color: colors.purple600,
  },
  ctaContact: {
    fontSize: 11,
    color: colors.slate600,
    lineHeight: 1.5,
  },
  ctaContactBold: {
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
  },
  ctaContactHighlight: {
    fontFamily: 'Helvetica-Bold',
    color: colors.emerald600,
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
});

const Page3 = () => (
  <Page size="A4" orientation="landscape" style={styles.page}>
    {/* Header */}
    <View style={styles.header}>
      <View style={styles.headerLeft}>
        <Text style={styles.headerTitle}>Why ApexPalantir</Text>
        <Text style={styles.headerSubtitle}>Engineering discipline for Salesforce that scales.</Text>
      </View>
      <View style={styles.headerRight}>
        <View style={styles.apBadge}>
          <Text style={styles.apText}>AP</Text>
        </View>
        <Text style={styles.catalogYear}>Service Catalog 2026</Text>
      </View>
    </View>

    {/* Hero Section */}
    <View style={styles.heroSection}>
      <View style={styles.heroLeft}>
        <Text style={styles.heroTitle}>
          We're Not Administrators—<Text style={styles.heroPurple}>We're Technical Architects</Text>
        </Text>
        <Text style={styles.heroSubtitle}>
          Founded by Computer Science & Infrastructure Engineering professionals who bring software engineering rigor to Salesforce.
        </Text>
        <View style={styles.decorativeLine}>
          <Svg width="96" height="4">
            <Rect x="0" y="0" width="96" height="4" fill={colors.brandGradientStart} rx="2" />
          </Svg>
        </View>
      </View>

      <View style={styles.heroRight}>
        <View style={styles.chartCard}>
          <Text style={styles.chartTitle}>Sustained Growth Trajectory</Text>

          {/* SVG Growth Chart */}
          <Svg width="320" height="140" viewBox="0 0 320 140">
            {/* Grid Lines */}
            <Line x1="40" y1="10" x2="40" y2="130" stroke="#CBD5E1" strokeWidth="2" />
            <Line x1="40" y1="130" x2="300" y2="130" stroke="#CBD5E1" strokeWidth="2" />

            {/* Growth Line */}
            <Path
              d="M 50 120 L 130 90 L 200 50 L 280 20"
              stroke={colors.brandGradientStart}
              strokeWidth="3"
              fill="none"
              strokeLinecap="round"
            />

            {/* Data Points */}
            <Circle cx="50" cy="120" r="5" fill="#8E2DE2" />
            <Circle cx="130" cy="90" r="5" fill="#8E2DE2" />
            <Circle cx="200" cy="50" r="5" fill="#8E2DE2" />
            <Circle cx="280" cy="20" r="6" fill="#4A00E0" />
          </Svg>

          <View style={styles.chartBottom}>
            <Text style={styles.chartLabel}>Built to scale from</Text>
            <Text style={styles.chartMetric}>$10M → $100M+</Text>
          </View>
        </View>
      </View>
    </View>

    {/* CTA Section */}
    <View style={styles.ctaSection}>
      <View style={styles.ctaGrid}>
        {/* Audit Card */}
        <View style={styles.ctaCard}>
          <View style={styles.ctaCardHeader}>
            <View style={styles.ctaIconBox}>
              <Svg width="20" height="20" viewBox="0 0 24 24">
                <Path
                  d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
              </Svg>
            </View>
            <Text style={styles.ctaCardTitle}>Start With a Technical Audit</Text>
          </View>
          <Text style={styles.ctaCardText}>
            Expose hidden technical debt before it breaks your revenue processes.
          </Text>
          <Text style={styles.ctaPrice}>€2,450</Text>
        </View>

        {/* Contact Card */}
        <View style={styles.ctaCard}>
          <View style={styles.ctaCardHeader}>
            <View style={styles.ctaIconBox}>
              <Svg width="20" height="20" viewBox="0 0 24 24">
                <Path
                  d="M13 17l5-5-5-5M6 17l5-5-5-5"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
              </Svg>
            </View>
            <Text style={styles.ctaCardTitle}>Get In Touch</Text>
          </View>
          <Text style={styles.ctaContact}>
            <Text style={styles.ctaContactBold}>Email: </Text>
            info@apexpalantir.com{'\n'}
            <Text style={styles.ctaContactBold}>Phone: </Text>
            +49 173 237 518 3{'\n'}
            <Text style={styles.ctaContactHighlight}>Response within 24 hours</Text>
          </Text>
        </View>
      </View>
    </View>

    {/* Footer */}
    <View style={styles.footer}>
      <View style={styles.footerLeft}>
        <Text style={commonStyles.footerText}>© 2026 ApexPalantir</Text>
        <Text style={commonStyles.footerText}>•</Text>
        <Text style={commonStyles.footerText}>Engineering Excellence</Text>
      </View>
      <View style={styles.footerRight}>
        <View style={styles.footerDot} />
        <Text style={commonStyles.footerTextLight}>Remote First. Europe Wide.</Text>
      </View>
    </View>
  </Page>
);

export default Page3;
