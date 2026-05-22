# Pazarat Frontend

Next.js frontend implementation for Pazarat.

## Technology Stack

- Next.js 15 (App Router)
- TypeScript 5
- Tailwind CSS
- React Hook Form + Zod
- shadcn/ui

## Structure

```
frontend/
├── src/
│   ├── app/                          # App Router
│   │   ├── (auth)/                   # Authentication routes
│   │   ├── (public)/                 # Public pages
│   │   ├── (admin)/                  # Admin dashboard
│   │   ├── (seller)/                 # Seller dashboard
│   │   ├── (buyer)/                  # Buyer dashboard
│   │   └── api/                     # API routes
│   ├── components/                   # Shared components
│   │   ├── ui/                      # UI components (shadcn/ui)
│   │   ├── layout/                  # Layout components
│   │   ├── shared/                  # Shared components
│   │   └── providers/               # Context providers
│   ├── lib/                          # Utilities
│   │   ├── api/                     # API client
│   │   ├── utils/                   # Utility functions
│   │   ├── hooks/                   # Custom hooks
│   │   └── constants/               # Constants
│   ├── features/                     # Feature modules
│   │   ├── admin/                   # Admin features
│   │   ├── seller/                  # Seller features
│   │   └── buyer/                   # Buyer features
│   ├── styles/                       # Global styles
│   └── types/                        # Global types
└── public/                           # Static assets
```

## Running

```bash
cd frontend
pnpm install
pnpm dev
```

## Building

```bash
pnpm build
```

## Testing

```bash
pnpm test
```
