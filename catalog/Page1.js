import React from 'react';
import { Page, Text, View, StyleSheet, Svg, Path, Line, Circle, Rect } from '@react-pdf/renderer';
import { colors, commonStyles } from './styles';

const styles = StyleSheet.create({
  page: {
    ...commonStyles.page,
  },
  header: {
    ...commonStyles.header,
    paddingBottom: 12,
  },
  logo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  logoBox: {
    width: 40,
    height: 40,
    backgroundColor: colors.brandGradientStart,
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logoText: {
    fontSize: 20,
    fontFamily: 'Helvetica-Bold',
    color: colors.slate900,
  },
  logoPurple: {
    color: colors.purple600,
  },
  headerRight: {
    fontSize: 11,
    color: colors.slate400,
    fontFamily: 'Helvetica-Bold',
    textTransform: 'uppercase',
    letterSpacing: 1.5,
  },
  heroSection: {
    height: '55%',
    paddingHorizontal: 64,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  heroLeft: {
    width: '50%',
    paddingRight: 32,
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
    maxWidth: 400,
  },
  decorativeLine: {
    marginTop: 32,
  },
  heroRight: {
    width: '50%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  codeWindow: {
    width: 480,
    backgroundColor: colors.slate900,
    borderRadius: 12,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: colors.slate700,
  },
  codeWindowHeader: {
    backgroundColor: colors.slate800,
    paddingHorizontal: 16,
    paddingVertical: 12,
    flexDirection: 'row',
    gap: 8,
    borderBottomWidth: 1,
    borderBottomColor: colors.slate700,
  },
  codeContent: {
    padding: 24,
    fontFamily: 'Courier',
    fontSize: 11,
  },
  codeLine: {
    flexDirection: 'row',
    marginBottom: 2,
  },
  lineNumber: {
    color: colors.slate500,
    width: 24,
  },
  codeKeyword: {
    color: '#A78BFA',
  },
  codeClass: {
    color: colors.yellow300,
  },
  codeComment: {
    color: colors.slate400,
  },
  codeMethod: {
    color: colors.blue400,
  },
  codeString: {
    color: colors.emerald400,
  },
  codeError: {
    color: '#F87171',
  },
  codeStatusBar: {
    backgroundColor: colors.slate900,
    borderTopWidth: 1,
    borderTopColor: colors.slate700,
    paddingHorizontal: 16,
    paddingVertical: 8,
    flexDirection: 'row',
    justifyContent: 'space-between',
    fontFamily: 'Courier',
    fontSize: 9,
  },
  valueSection: {
    height: '30%',
    paddingHorizontal: 64,
    paddingBottom: 24,
  },
  valueGrid: {
    flexDirection: 'row',
    gap: 32,
    height: '100%',
  },
  valueCard: {
    flex: 1,
    backgroundColor: colors.slate50,
    borderRadius: 16,
    padding: 24,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    justifyContent: 'center',
  },
  valueCardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 8,
  },
  valueIconBox: {
    padding: 8,
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
  },
  valueCardTitle: {
    fontFamily: 'Helvetica-Bold',
    fontSize: 16,
    color: colors.slate900,
  },
  valueCardText: {
    fontSize: 11,
    color: colors.slate600,
    lineHeight: 1.5,
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

const Page1 = () => (
  <Page size="A4" orientation="landscape" style={styles.page}>
    {/* Header */}
    <View style={styles.header}>
      <View style={styles.logo}>
        <View style={styles.logoBox}>
          <Svg width="24" height="24" viewBox="0 0 24 24">
            <Path
              d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"
              fill="white"
            />
          </Svg>
        </View>
        <Text style={styles.logoText}>
          Apex<Text style={styles.logoPurple}>Palantir</Text>
        </Text>
      </View>
      <Text style={styles.headerRight}>Service Catalog 2026</Text>
    </View>

    {/* Hero Section */}
    <View style={styles.heroSection}>
      <View style={styles.heroLeft}>
        <Text style={styles.heroTitle}>
          Engineering Discipline for <Text style={styles.heroPurple}>Salesforce That Scales</Text>
        </Text>
        <Text style={styles.heroSubtitle}>
          Most Salesforce instances collapse under technical debt within 5 years. We architect systems built to last—and grow—forever.
        </Text>
        <View style={styles.decorativeLine}>
          <Svg width="96" height="4">
            <Rect x="0" y="0" width="96" height="4" fill={colors.brandGradientStart} rx="2" />
          </Svg>
        </View>
      </View>

      <View style={styles.heroRight}>
        <View style={styles.codeWindow}>
          <View style={styles.codeWindowHeader}>
            <Svg width="12" height="12">
              <Circle cx="6" cy="6" r="6" fill={colors.red500} />
            </Svg>
            <Svg width="12" height="12">
              <Circle cx="6" cy="6" r="6" fill={colors.yellow500} />
            </Svg>
            <Svg width="12" height="12">
              <Circle cx="6" cy="6" r="6" fill={colors.emerald500} />
            </Svg>
          </View>
          <View style={styles.codeContent}>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>1</Text>
              <Text style={styles.codeKeyword}>class </Text>
              <Text style={styles.codeClass}>RevOpsArchitecture </Text>
              <Text style={{color: colors.slate300}}>{'{'}</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>2</Text>
              <Text style={styles.codeComment}>  // Stop patching. Start architecting.</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>3</Text>
              <Text style={styles.codeKeyword}>  public static void</Text>
              <Text style={styles.codeMethod}> scaleGrowth</Text>
              <Text style={{color: colors.slate300}}>{'() {'}</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>4</Text>
              <Text style={styles.codeKeyword}>    if </Text>
              <Text style={{color: colors.slate300}}>{'(technicalDebt '}</Text>
              <Text style={styles.codeKeyword}>{'> '}</Text>
              <Text style={styles.codeError}>LIMIT</Text>
              <Text style={{color: colors.slate300}}>{') {'}</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>5</Text>
              <Text style={styles.codeComment}>      // This is what we prevent</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>6</Text>
              <Text style={styles.codeError}>      throw new SystemCollapseException();</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>7</Text>
              <Text style={{color: colors.slate300}}>{'    }'}</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>8</Text>
              <Text style={styles.codeString}>    return </Text>
              <Text style={styles.codeClass}>SustainedRevenue</Text>
              <Text style={{color: colors.slate300}}>;</Text>
            </View>
            <View style={styles.codeLine}>
              <Text style={styles.lineNumber}>9</Text>
              <Text style={{color: colors.slate300}}>{'}'}</Text>
            </View>
          </View>
          <View style={styles.codeStatusBar}>
            <Text style={{color: colors.slate400}}>main.apex</Text>
            <Text style={{color: colors.emerald400}}>● No Errors Found</Text>
          </View>
        </View>
      </View>
    </View>

    {/* Value Blocks */}
    <View style={styles.valueSection}>
      <View style={styles.valueGrid}>
        <View style={styles.valueCard}>
          <View style={styles.valueCardHeader}>
            <View style={styles.valueIconBox}>
              <Svg width="20" height="20" viewBox="0 0 24 24">
                <Path
                  d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
              </Svg>
            </View>
            <Text style={styles.valueCardTitle}>Eliminate Revenue Risk</Text>
          </View>
          <Text style={styles.valueCardText}>
            Stop fearing your own CRM. We map every hidden dependency so you can scale without breaking critical sales flows.
          </Text>
        </View>

        <View style={styles.valueCard}>
          <View style={styles.valueCardHeader}>
            <View style={styles.valueIconBox}>
              <Svg width="20" height="20" viewBox="0 0 24 24">
                <Path
                  d="M13 17l5-5-5-5M6 17l5-5-5-5"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
              </Svg>
            </View>
            <Text style={styles.valueCardTitle}>Unblock Strategy</Text>
          </View>
          <Text style={styles.valueCardText}>
            Never let IT be the bottleneck. We build flexible architectures that let you launch new products and territories instantly.
          </Text>
        </View>

        <View style={styles.valueCard}>
          <View style={styles.valueCardHeader}>
            <View style={styles.valueIconBox}>
              <Svg width="20" height="20" viewBox="0 0 24 24">
                <Path
                  d="M22 11.08V12a10 10 0 1 1-5.93-9.14"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
                <Path
                  d="M22 4L12 14.01l-3-2.99"
                  fill="none"
                  stroke={colors.brandGradientStart}
                  strokeWidth="2"
                />
              </Svg>
            </View>
            <Text style={styles.valueCardTitle}>Sustained Growth</Text>
          </View>
          <Text style={styles.valueCardText}>
            Break the 5-year technical debt cycle. We build a foundation that supports your company from $10M to $100M+ revenue.
          </Text>
        </View>
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
      </View>
    </View>
  </Page>
);

export default Page1;
