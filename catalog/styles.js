import { StyleSheet } from '@react-pdf/renderer';

// Brand colors
export const colors = {
  brandGradientStart: '#8E2DE2',
  brandGradientEnd: '#4A00E0',
  purple600: '#9333EA',
  purple50: '#FAF5FF',
  slate50: '#F8FAFC',
  slate200: '#E2E8F0',
  slate300: '#CBD5E1',
  slate400: '#94A3B8',
  slate500: '#64748B',
  slate600: '#475569',
  slate700: '#334155',
  slate800: '#1E293B',
  slate900: '#0F172A',
  emerald400: '#34D399',
  emerald500: '#10B981',
  emerald600: '#059669',
  red500: '#EF4444',
  yellow300: '#FCD34D',
  yellow500: '#F59E0B',
  blue400: '#60A5FA',
  orange400: '#FB923C',
};

// Common styles shared across pages
export const commonStyles = StyleSheet.create({
  page: {
    width: '297mm',
    height: '210mm',
    fontFamily: 'Helvetica',
    backgroundColor: '#FFFFFF',
    flexDirection: 'column',
  },
  header: {
    height: '10%',
    paddingHorizontal: 64,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: colors.slate200,
  },
  footer: {
    height: '5%',
    backgroundColor: colors.slate900,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 64,
  },
  footerText: {
    fontSize: 11,
    color: colors.slate400,
  },
  footerTextLight: {
    fontSize: 11,
    color: colors.slate300,
    fontFamily: 'Helvetica-Bold',
  },
});
