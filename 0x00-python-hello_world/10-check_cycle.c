#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a linked has a cycle
 *
 * @list: Pointer to the head of the linked list
 * Return: 1 if the list cycle 0 if not cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
