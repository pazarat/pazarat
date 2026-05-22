# PAZARAT FRONTEND NEXT.JS STRUCTURE

# Purpose

This file defines the detailed frontend structure for Pazarat using Next.js App Router, TypeScript, and modern React patterns.

It is the operational blueprint for frontend code generation, implementation, and development workflow.

---

# Technology Stack

```txt
Framework: Next.js 15 (App Router)
Language: TypeScript 5
Styling: Tailwind CSS + CSS Modules
Forms: React Hook Form + Zod
State Management: React Context + Zustand (optional)
Data Fetching: Next.js Server Components + SWR/React Query
Testing: Vitest, React Testing Library, Playwright
Build Tool: Turbopack (Next.js built-in)
Package Manager: pnpm
```

---

# Project Structure

```
frontend/
├── src/
│   ├── app/                        # App Router
│   │   ├── (auth)/                # Auth layout group
│   │   │   ├── login/
│   │   │   │   └── page.tsx
│   │   │   ├── register/
│   │   │   │   └── page.tsx
│   │   │   └── layout.tsx
│   │   │
│   │   ├── (public)/              # Public layout group
│   │   │   ├── page.tsx           # Home page
│   │   │   ├── about/
│   │   │   │   └── page.tsx
│   │   │   └── layout.tsx
│   │   │
│   │   ├── (admin)/               # Admin dashboard layout group
│   │   │   ├── dashboard/
│   │   │   │   └── page.tsx
│   │   │   ├── governance/
│   │   │   │   └── page.tsx
│   │   │   ├── users/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── [id]/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── create/
│   │   │   │       └── page.tsx
│   │   │   ├── merchants/
│   │   │   │   └── page.tsx
│   │   │   ├── orders/
│   │   │   │   └── page.tsx
│   │   │   ├── financial/
│   │   │   │   └── page.tsx
│   │   │   ├── marketing/
│   │   │   │   └── page.tsx
│   │   │   ├── operations/
│   │   │   │   └── page.tsx
│   │   │   ├── smart-data/
│   │   │   │   └── page.tsx
│   │   │   └── system/
│   │   │       └── page.tsx
│   │   │   └── layout.tsx
│   │   │
│   │   ├── (seller)/              # Seller dashboard layout group
│   │   │   ├── dashboard/
│   │   │   │   └── page.tsx
│   │   │   ├── products/
│   │   │   │   └── page.tsx
│   │   │   ├── orders/
│   │   │   │   └── page.tsx
│   │   │   └── layout.tsx
│   │   │
│   │   ├── (buyer)/               # Buyer dashboard layout group
│   │   │   ├── dashboard/
│   │   │   │   └── page.tsx
│   │   │   ├── orders/
│   │   │   │   └── page.tsx
│   │   │   └── layout.tsx
│   │   │
│   │   ├── api/                   # API routes
│   │   │   ├── auth/
│   │   │   │   └── [...nextauth]/
│   │   │   │       └── route.ts
│   │   │   └── users/
│   │   │       └── route.ts
│   │   │
│   │   ├── layout.tsx             # Root layout
│   │   ├── page.tsx               # Root page
│   │   ├── globals.css            # Global styles
│   │   └── error.tsx              # Error boundary
│   │
│   ├── components/                # Shared components
│   │   ├── ui/                    # UI components (shadcn/ui)
│   │   │   ├── button/
│   │   │   │   ├── button.tsx
│   │   │   │   └── index.ts
│   │   │   ├── input/
│   │   │   │   ├── input.tsx
│   │   │   │   └── index.ts
│   │   │   ├── table/
│   │   │   │   ├── table.tsx
│   │   │   │   └── index.ts
│   │   │   ├── dialog/
│   │   │   │   ├── dialog.tsx
│   │   │   │   └── index.ts
│   │   │   ├── dropdown-menu/
│   │   │   │   ├── dropdown-menu.tsx
│   │   │   │   └── index.ts
│   │   │   └── ...
│   │   │
│   │   ├── layout/                # Layout components
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Navigation.tsx
│   │   │
│   │   ├── shared/                # Shared components
│   │   │   ├── LoadingSpinner.tsx
│   │   │   ├── ErrorBoundary.tsx
│   │   │   ├── EmptyState.tsx
│   │   │   └── Pagination.tsx
│   │   │
│   │   └── providers/             # Context providers
│   │       ├── AuthProvider.tsx
│   │       ├── ThemeProvider.tsx
│   │       └── QueryProvider.tsx
│   │
│   ├── lib/                       # Utilities
│   │   ├── api/                   # API client
│   │   │   ├── client.ts
│   │   │   ├── users.ts
│   │   │   └── ...
│   │   ├── utils/                 # Utility functions
│   │   │   ├── cn.ts
│   │   │   ├── format.ts
│   │   │   └── validation.ts
│   │   ├── hooks/                 # Custom hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useUsers.ts
│   │   │   └── ...
│   │   └── constants/             # Constants
│   │       ├── api.ts
│   │       └── routes.ts
│   │
│   ├── features/                  # Feature modules
│   │   ├── auth/                  # Authentication
│   │   │   ├── components/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   └── RegisterForm.tsx
│   │   │   ├── hooks/
│   │   │   │   └── useAuth.ts
│   │   │   └── types/
│   │   │       └── auth.ts
│   │   │
│   │   ├── admin/                 # Admin dashboard
│   │   │   ├── governance/
│   │   │   │   ├── components/
│   │   │   │   │   ├── CountryContextForm.tsx
│   │   │   │   │   └── GovernanceRulesTable.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useGovernance.ts
│   │   │   │
│   │   │   ├── users/
│   │   │   │   ├── components/
│   │   │   │   │   ├── UsersTable.tsx
│   │   │   │   │   ├── UserForm.tsx
│   │   │   │   │   ├── UserFilters.tsx
│   │   │   │   │   └── UserDetail.tsx
│   │   │   │   ├── hooks/
│   │   │   │   │   ├── useUsers.ts
│   │   │   │   │   └── useUser.ts
│   │   │   │   └── types/
│   │   │   │       └── user.ts
│   │   │   │
│   │   │   ├── merchants/
│   │   │   │   ├── components/
│   │   │   │   │   ├── MerchantsTable.tsx
│   │   │   │   │   └── MerchantForm.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useMerchants.ts
│   │   │   │
│   │   │   ├── orders/
│   │   │   │   ├── components/
│   │   │   │   │   ├── OrdersTable.tsx
│   │   │   │   │   └── OrderDetail.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useOrders.ts
│   │   │   │
│   │   │   ├── financial/
│   │   │   │   ├── components/
│   │   │   │   │   ├── PaymentsTable.tsx
│   │   │   │   │   └── WalletsTable.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useFinancial.ts
│   │   │   │
│   │   │   ├── marketing/
│   │   │   │   ├── components/
│   │   │   │   │   ├── CampaignsTable.tsx
│   │   │   │   │   └── CouponsTable.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useMarketing.ts
│   │   │   │
│   │   │   ├── operations/
│   │   │   │   ├── components/
│   │   │   │   │   ├── ShipmentsTable.tsx
│   │   │   │   │   └── WarehousesTable.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useOperations.ts
│   │   │   │
│   │   │   ├── smart-data/
│   │   │   │   ├── components/
│   │   │   │   │   ├── ReportsTable.tsx
│   │   │   │   │   └── AnalyticsDashboard.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useSmartData.ts
│   │   │   │
│   │   │   └── system/
│   │   │       ├── components/
│   │   │       │   ├── RolesTable.tsx
│   │   │       │   └── PermissionsTable.tsx
│   │   │       └── hooks/
│   │   │           └── useSystem.ts
│   │   │
│   │   ├── seller/                # Seller dashboard
│   │   │   ├── components/
│   │   │   │   ├── SellerDashboard.tsx
│   │   │   │   └── SellerProducts.tsx
│   │   │   └── hooks/
│   │   │       └── useSeller.ts
│   │   │
│   │   └── buyer/                 # Buyer dashboard
│   │       ├── components/
│   │       │   ├── BuyerDashboard.tsx
│   │       │   └── BuyerOrders.tsx
│   │       └── hooks/
│   │           └── useBuyer.ts
│   │
│   ├── styles/                    # Styles
│   │   ├── globals.css
│   │   └── components.css
│   │
│   └── types/                     # Global types
│       ├── api.ts
│       └── common.ts
│
├── public/                        # Static assets
│   ├── images/
│   ├── icons/
│   └── fonts/
│
├── tests/                         # Tests
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── .env.example                   # Environment variables example
├── .env.local                     # Local environment variables
├── next.config.js                 # Next.js configuration
├── tailwind.config.ts             # Tailwind configuration
├── tsconfig.json                  # TypeScript configuration
├── package.json                   # Dependencies
├── pnpm-lock.yaml                 # Lock file
└── README.md                      # Frontend README
```

---

# App Router Structure

## Route Groups
Route groups organize routes without affecting URL structure:

- `(auth)` - Authentication routes
- `(public)` - Public pages
- `(admin)` - Admin dashboard
- `(seller)` - Seller dashboard
- `(buyer)` - Buyer dashboard

## Layouts
Each route group has its own layout:

```typescript
// app/(admin)/layout.tsx
export default function AdminLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1">
        <Header />
        <main className="p-6">{children}</main>
      </div>
    </div>
  )
}
```

---

# Component Structure

## UI Components (shadcn/ui)
```typescript
// components/ui/button/button.tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline: "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
```

## Feature Components
```typescript
// features/admin/users/components/UsersTable.tsx
"use client"

import { useState } from "react"
import { useUsers } from "../hooks/useUsers"
import { Button } from "@/components/ui/button"
import { Table } from "@/components/ui/table"
import { UserFilters } from "./UserFilters"

export function UsersTable() {
  const [filters, setFilters] = useState({})
  const { data, isLoading, error } = useUsers(filters)

  if (isLoading) return <LoadingSpinner />
  if (error) return <ErrorState error={error} />

  return (
    <div className="space-y-4">
      <UserFilters filters={filters} onFiltersChange={setFilters} />
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Email</TableHead>
            <TableHead>Name</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {data?.users.map((user) => (
            <TableRow key={user.id}>
              <TableCell>{user.email}</TableCell>
              <TableCell>{user.firstName} {user.lastName}</TableCell>
              <TableCell>{user.status}</TableCell>
              <TableCell>
                <Button variant="ghost" size="sm">View</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
```

---

# API Client

## Base Client
```typescript
// lib/api/client.ts
import axios from "axios"

const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000/api",
  headers: {
    "Content-Type": "application/json",
  },
})

// Request interceptor
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("token")
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      window.location.href = "/login"
    }
    return Promise.reject(error)
  }
)

export default apiClient
```

## Typed API Calls
```typescript
// lib/api/users.ts
import apiClient from "./client"
import type { User, CreateUserDto, UpdateUserDto } from "@/types/api"

export const usersApi = {
  getAll: (params?: Record<string, any>) =>
    apiClient.get<{ users: User[]; total: number }>("/users", { params }),
  
  getById: (id: string) =>
    apiClient.get<User>(`/users/${id}`),
  
  create: (data: CreateUserDto) =>
    apiClient.post<User>("/users", data),
  
  update: (id: string, data: UpdateUserDto) =>
    apiClient.put<User>(`/users/${id}`, data),
  
  delete: (id: string) =>
    apiClient.delete(`/users/${id}`),
}
```

---

# Custom Hooks

## useAuth Hook
```typescript
// lib/hooks/useAuth.ts
import { useState, useEffect } from "react"
import type { User } from "@/types/api"

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Check if user is authenticated
    const token = localStorage.getItem("token")
    if (token) {
      // Fetch user data
      fetchUser()
    } else {
      setIsLoading(false)
    }
  }, [])

  const fetchUser = async () => {
    try {
      const response = await fetch("/api/auth/me")
      const data = await response.json()
      setUser(data.user)
    } catch (error) {
      console.error("Failed to fetch user:", error)
    } finally {
      setIsLoading(false)
    }
  }

  const login = async (email: string, password: string) => {
    // Implement login
  }

  const logout = () => {
    localStorage.removeItem("token")
    setUser(null)
    window.location.href = "/login"
  }

  return { user, isLoading, login, logout }
}
```

## useUsers Hook
```typescript
// features/admin/users/hooks/useUsers.ts
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { usersApi } from "@/lib/api/users"
import type { User } from "@/types/api"

export function useUsers(filters: Record<string, any> = {}) {
  return useQuery({
    queryKey: ["users", filters],
    queryFn: () => usersApi.getAll(filters),
  })
}

export function useUser(id: string) {
  return useQuery({
    queryKey: ["user", id],
    queryFn: () => usersApi.getById(id),
  })
}

export function useCreateUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: usersApi.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })
}

export function useUpdateUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: any }) =>
      usersApi.update(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })
}

export function useDeleteUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: usersApi.delete,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })
}
```

---

# Types

## API Types
```typescript
// types/api.ts
export interface User {
  id: string
  email: string
  firstName: string
  lastName: string
  status: "Active" | "Inactive" | "Pending"
  createdAt: string
  updatedAt?: string
}

export interface CreateUserDto {
  email: string
  firstName: string
  lastName: string
}

export interface UpdateUserDto {
  firstName?: string
  lastName?: string
  status?: "Active" | "Inactive" | "Pending"
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
}

export interface ApiError {
  message: string
  errors?: Record<string, string[]>
}
```

---

# Configuration Files

## next.config.js
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ["localhost"],
  },
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  },
}

module.exports = nextConfig
```

## tailwind.config.ts
```typescript
import type { Config } from "tailwindcss"

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}

export default config
```

## tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

---

# Testing

## Unit Tests
```typescript
// tests/unit/components/Button.test.tsx
import { render, screen } from "@testing-library/react"
import { Button } from "@/components/ui/button"

describe("Button", () => {
  it("renders correctly", () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText("Click me")).toBeInTheDocument()
  })
})
```

## E2E Tests
```typescript
// tests/e2e/admin/users.spec.ts
import { test, expect } from "@playwright/test"

test("should display users table", async ({ page }) => {
  await page.goto("/admin/users")
  await expect(page.locator("table")).toBeVisible()
})
```

---

# This Structure Aligns With

- Pazarat 360-degree engineering method
- Next.js 15 App Router best practices
- TypeScript strict mode
- Server Components first
- Client Components where needed
- React Hook Form + Zod for forms
- Tailwind CSS for styling
- shadcn/ui for components
- SWR/React Query for data fetching
- Pazarat business domains
- Scalable feature modules
- Type-safe API calls
- Test-driven development
- CI/CD readiness

This structure is the foundation for building a modern, scalable, and maintainable frontend for Pazarat.
