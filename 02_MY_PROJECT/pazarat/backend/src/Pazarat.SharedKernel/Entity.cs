namespace Pazarat.SharedKernel;

public abstract class Entity<TId>
{
    public TId Id { get; protected init; } = default!;
}
